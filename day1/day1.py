## Part 1
dial_num_one = 50
res_one = 0

with open("day1.txt", "r") as file:
    for line in file:
        direction = line.strip()[0]
        steps = int(line.strip()[1:])

        if direction == "L":
            dial_num_one = (dial_num_one - steps) % 100
        else:
            dial_num_one = (dial_num_one + steps) % 100

        if dial_num_one == 0:
            res_one += 1

print(res_one)


## Part 2
dial_num_two = 50
res_two = 0

with open("day1.txt", "r") as file:
    for line in file:
        direction = line.strip()[0]
        steps = int(line.strip()[1:])

        if direction == "L":
            if dial_num_two != 0 and dial_num_two - steps <= 0:
                res_two += 1
                steps_left = steps - dial_num_two
                res_two += steps_left // 100
            elif dial_num_two == 0:
                res_two += steps // 100
            dial_num_two = (dial_num_two - steps) % 100
        else:
            if dial_num_two != 0 and dial_num_two + steps >= 100:
                res_two += 1
                steps_left = steps - (100 - dial_num_two)
                res_two += steps_left // 100
            elif dial_num_two == 0:
                res_two += steps // 100
            dial_num_two = (dial_num_two + steps) % 100

print(res_two)
