import re

with open('p1input.txt') as f:
    read_data = list(f)

valid_passwords = 0

for line in read_data:
    char_count = 0

    minimum_term = re.compile('\d\d?-')
    minimum = int(minimum_term.search(line).group().rsplit('-')[0])

    maximum_term = re.compile('-\d\d?')
    maximum = int(maximum_term.search(line).group().split('-')[1])

    character_term = re.compile('[a-zA-Z]:')
    character = character_term.search(line).group().rsplit(':')[0]

    password = line.split(': ')[1]

    for char in password:
        if char == character:
            char_count = char_count + 1

    if ((char_count >= minimum) and (char_count <= maximum)):
        valid_passwords = valid_passwords + 1

print(valid_passwords)
