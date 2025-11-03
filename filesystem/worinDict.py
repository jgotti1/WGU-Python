synonyms = {}   # Define dictionary

user_input = input().split()

with open(f"{user_input[0]}.txt", "r") as file:
    content_list = file.readlines()
content_list = [line.strip() for line in content_list]

for word in content_list:
    synonyms[word[:1]] = word.split()


if user_input[1] in synonyms:
    output_values = synonyms[user_input[1]]
    
    for value in output_values:
        print(value)

else: 
    print(f"No synonyms for educate begin with {user_input[1]}.")





