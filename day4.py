import re
def values_within_bounds(regex_result,upper,lower):
    value = int(regex_result.group(1))
    return value < upper and value > lower

def field_is_valid(field_name, input_string):
    '''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''
    regex_expression = field_name+'\:(\w+)'
    result = re.search(regex_expression, input_string)
    
    if result:
        if field_name == 'byr':
            return values_within_bounds(result, 1920, 2002)
        if field_name == "cid":
            return values_within_bounds(result, 0, 2000)

        

passports = []
with open('day4.input') as input_file:
    passport = ""
    lines = input_file.readlines()
    last = lines[-1]
    for line in lines:
        if line == "\n":
            passports.append(passport)
            passport = ""
        else:
            passport = passport + line
            if line is last:
                passports.append(passport)


mandatory_fields = ["byr"]#, "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]

valid_passports = 0
for passport in passports:
    passport_valid = True
    i = 0
    while passport_valid and i < len(mandatory_fields):
        if not field_is_valid(mandatory_fields[i], passport):
            passport_valid = False
        i = i + 1
    if passport_valid:
        valid_passports = valid_passports + 1
            

        

print(valid_passports)
