# Read input file name
file_name = input()

students = []
mid1_total = 0
mid2_total = 0
final_total = 0
count = 0

with open(file_name, 'r') as file:
    for line in file:
        parts = line.strip().split("\t")
        last = parts[0]
        first = parts[1]
        mid1 = int(parts[2])
        mid2 = int(parts[3])
        final = int(parts[4])

        avg = (mid1 + mid2 + final) / 3

        # Assign letter grade
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        else:
            grade = "F"

        students.append([last, first, mid1, mid2, final, grade])

        # Accumulate exam totals
        mid1_total += mid1
        mid2_total += mid2
        final_total += final
        count += 1

# Compute averages
mid1_avg = mid1_total / count
mid2_avg = mid2_total / count
final_avg = final_total / count

# Write to report.txt
with open("report.txt", "w") as out:
    for s in students:
        out.write(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\n")
    out.write(f"\nAverages: midterm1 {mid1_avg:.2f}, midterm2 {mid2_avg:.2f}, final {final_avg:.2f}")
