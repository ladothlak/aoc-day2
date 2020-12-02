import re

with open('p1input.txt') as f:
    read_data = list(f)

valid_passwords = 0

for line in read_data:
    char_count = 0

    pos_one_term = re.compile('\d\d?-')
    pos_one = int(pos_one_term.search(line).group().rsplit('-')[0]) - 1

    pos_two_term = re.compile('-\d\d?')
    pos_two = int(pos_two_term.search(line).group().split('-')[1]) - 1

    character_term = re.compile('[a-zA-Z]:')
    character = character_term.search(line).group().rsplit(':')[0]

    password = line.split(': ')[1]

    password_pos_one = (password[pos_one] == character)
    password_pos_two = (password[pos_two] == character)

    if ((password_pos_one and not password_pos_two) or (password_pos_two and not password_pos_one)):
        valid_passwords = valid_passwords + 1

print(valid_passwords)
