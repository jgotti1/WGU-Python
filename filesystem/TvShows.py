file_name = input()
show_dict = {}

# Read lines from input file
with open(file_name, 'r') as show_file:
    lines = show_file.readlines()

# Build dictionary: seasons -> list of shows
for i in range(0, len(lines), 2):
    seasons = int(lines[i].strip())
    show = lines[i + 1].strip()

    if seasons not in show_dict:
        show_dict[seasons] = []
    show_dict[seasons].append(show)

# --- Output 1: Sort dictionary by key (descending) ---
with open("output_keys.txt", "w") as out1:
    for seasons in sorted(show_dict.keys(), reverse=True):
        shows = "; ".join(show_dict[seasons])  # Join multiple shows with semicolon
        out1.write(f"{seasons}: {shows}\n")

# --- Output 2: Sort by show titles (reverse alphabetical) ---
all_shows = []
for show_list in show_dict.values():
    all_shows.extend(show_list)

all_shows.sort(reverse=True)

with open("output_titles.txt", "w") as out2:
    for show in all_shows:
        out2.write(show + "\n")
