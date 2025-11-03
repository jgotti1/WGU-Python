file_name = input()

with open(file_name, 'r') as file:
    for line in file:
        photo = line.strip()
        info_file = photo.replace("_photo.jpg", "_info.txt")
        print(info_file)
