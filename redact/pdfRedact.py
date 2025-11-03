#!/usr/bin/env python3
import re
from pathlib import Path
import fitz  # PyMuPDF


# ------------------ Pattern / Detection Helpers ------------------ #

def luhn_check(number: str) -> bool:
    digits = [int(d) for d in number if d.isdigit()]
    if len(digits) < 12:
        return False
    checksum = 0
    parity = len(digits) % 2
    for i, d in enumerate(digits):
        if i % 2 == parity:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d
    return checksum % 10 == 0


def is_ssn(text: str) -> bool:
    digits = re.sub(r"\D", "", text)
    return len(digits) == 9 and not (
        digits.startswith("000") or digits[3:5] == "00" or digits[5:] == "0000"
    )


def is_credit_card(text: str) -> bool:
    digits = re.sub(r"\D", "", text)
    return 13 <= len(digits) <= 19 and luhn_check(digits)


def is_routing_number(text: str) -> bool:
    digits = re.sub(r"\D", "", text)
    return len(digits) == 9


def looks_like_account(text: str, left: str, right: str) -> bool:
    digits = re.sub(r"\D", "", text)
    if not 6 <= len(digits) <= 17:
        return False
    keywords = ["account", "acct", "acct#", "a/c", "account#", "account number"]
    context = (left + " " + right).lower()
    return any(k in context for k in keywords)


def is_numericish(word: str) -> bool:
    """Return True if word is composed of digits and/or hyphens."""
    return bool(re.fullmatch(r"[0-9\-]+", word))


# ------------------ PDF Redaction Core (Final Correct Version) ------------------ #

def redact_pdf(input_file: Path, output_file: Path, expand=1.05):
    doc = fitz.open(input_file)
    total_hits = 0

    for page in doc:
        words = page.get_text("words")
        words.sort(key=lambda w: (round(w[1], 1), round(w[0], 1)))
        text_list = [w[4] for w in words]

        rects = []
        max_group = 4  # only group up to 4 NUMERIC words

        for i in range(len(words)):
            for length in range(1, max_group + 1):
                if i + length > len(words):
                    break

                chunk = words[i:i+length]
                texts = [w[4] for w in chunk]

                # ✅ *Only* group if all parts are numeric-like (prevents full-line grabbing)
                if not all(is_numericish(t) for t in texts):
                    continue

                seq = " ".join(texts)
                left = " ".join(text_list[max(0, i-5):i])
                right = " ".join(text_list[i+length:i+length+5])

                if (
                    is_ssn(seq)
                    or is_credit_card(seq)
                    or is_routing_number(seq)
                    or looks_like_account(seq, left, right)
                ):
                    # Tight bounding box on just the grouped number
                    x0 = min(w[0] for w in chunk)
                    y0 = min(w[1] for w in chunk)
                    x1 = max(w[2] for w in chunk)
                    y1 = max(w[3] for w in chunk)

                    pad_x = (x1 - x0) * (expand - 1)
                    pad_y = (y1 - y0) * (expand - 1)

                    rect = fitz.Rect(x0 - pad_x, y0 - pad_y, x1 + pad_x, y1 + pad_y)
                    rects.append(rect)
                    total_hits += 1
                    break  # stop expanding this sequence

        for r in rects:
            page.add_redact_annot(r, fill=(0, 0, 0))

        if rects:
            page.apply_redactions()

    doc.save(output_file, deflate=True)
    doc.close()
    return total_hits


# ------------------ Folder Batch Mode ------------------ #

def main():
    input_folder = Path("input_pdfs")
    output_folder = Path("output_redacted")

    input_folder.mkdir(exist_ok=True)
    output_folder.mkdir(exist_ok=True)

    print("\n📂 Input Folder:", input_folder.resolve())
    print("💾 Output Folder:", output_folder.resolve(), "\n")

    pdfs = list(input_folder.glob("*.pdf"))
    if not pdfs:
        print("⚠ No PDFs found. Put files into input_pdfs and run again.")
        return

    for pdf in pdfs:
        out_file = output_folder / f"{pdf.stem}_redacted.pdf"
        print(f"→ Redacting {pdf.name} ...")
        hits = redact_pdf(pdf, out_file)
        print(f"   ✓ {hits} item(s) redacted → {out_file.name}")

    print("\n✅ Redaction complete.\n")
    
    



if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")