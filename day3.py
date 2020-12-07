from operator import mul
input = []

with open('day3.input') as input_file:
    for line in input_file:
        new_list = []
        for character in line:
            if character != '\n':
                new_list.append(character)
        input.append(new_list)


slopes_part_one = [(3,1)]
slopes_part_two = [(1,1),(3,1),(5,1),(7,1),(1,2)]
total_number_of_trees = []
for slope in slopes_part_two:
    i = 0
    j = 0

    di = slope[0]
    dj = slope[1]

    number_of_trees = 0
    while j < len(input):
        i_actual = i % len(input[j])
        if input[j][i_actual] is "#":
            number_of_trees = number_of_trees + 1

        i = i + di
        j = j + dj
    total_number_of_trees.append(number_of_trees)
print(total_number_of_trees)
print(reduce(mul, total_number_of_trees, 1))
