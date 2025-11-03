# String replace_string is read from input. Then, sentence is read from input. If replace_string is in sentence, then:

# Output "Located at index: " followed by the index of the first occurrence.
# Create a string from sentence with all occurrences of replace_string replaced by "##" and output the new string on a new line.

# Otherwise, output "No results"

replace_string = input()
sentence = input()

if replace_string in sentence:
    print(f'Located at index: {sentence.find(replace_string)}')
    new_sentence = sentence.replace(replace_string, '##')
    print(new_sentence)
else:
    print('No results')
