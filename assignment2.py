# create an empty dictionary
ascii_dict = {}

# loop through the alphabet
for letter in range(97, 123):
    # add the letter and its ASCII value to the dictionary
    ascii_dict[chr(letter)] = letter

# print the dictionary
print(ascii_dict)
