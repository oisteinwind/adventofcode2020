def get_lower_bound(input):
    splitted_string = input.split('-')
    return int(splitted_string[0])
def get_upper_bound(input):
    splitted_string = input.split('-')
    next_splitted_string = splitted_string[1].split(' ')
    return int(next_splitted_string[0])
def get_special_character(input):
    splitted_string = input.split(':')
    return splitted_string[0][-1]
def get_password(input):
    splitted_string = input.split(':')
    return splitted_string[1].strip()
def password_is_valid(input):
    special_character = get_special_character(input)
    password = get_password(input)
    occurences = password.count(special_character)
    lower_bound = get_lower_bound(input)
    upper_bound = get_upper_bound(input)
    if occurences <= upper_bound and lower_bound <= occurences:
        return True
    return False
def characters_in_right_place(input):
    password = get_password(input)
    special_character = get_special_character(input)
    first_position = get_lower_bound(input)-1
    second_position = get_upper_bound(input)-1
    if len(password) < second_position:
        return False
    if password[first_position] is special_character and password[second_position] is not special_character:
        return True
    if password[first_position] is not special_character and password[second_position] is special_character:
        return True
    return False

with open('day2.input') as input_file:
    input = input_file.read().splitlines() 

valid_passwords = 0
for line in input:
    if password_is_valid(line):
        valid_passwords = valid_passwords + 1
print('Valid passwords: ' + str(valid_passwords))

valid_passwords_part_two = 0
for line in input:
    if characters_in_right_place(line):
        valid_passwords_part_two = valid_passwords_part_two + 1
print('Valid passwords part two: ' + str(valid_passwords_part_two))
