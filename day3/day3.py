from operator import indexOf

## Part 1
banks = []
res_one = 0


def find_max_first(bank):
    max_num = max(bank)
    max_num_idx = indexOf(bank, max_num)

    if max_num_idx == len(bank) - 1:
        bank = bank[:max_num_idx]
        max_num = max(bank)

    return max_num


with open("day3.txt", "r") as file:
    for line in file:
        banks.append(line.strip())

for bank in banks:
    max_first_num = find_max_first(bank)
    bank = bank[indexOf(bank, max_first_num) + 1 :]
    max_second_num = max(bank)
    res_one += int(max_first_num) * 10 + int(max_second_num)

print(res_one)


## Part 2
banks = []
joltages = []
res_two = 0


def find_max_battery(bank, num_still_needed):
    bank_to_check = bank[: len(bank) - num_still_needed + 1]
    max_battery = max(bank_to_check)
    max_battery_idx = indexOf(bank_to_check, max_battery)
    return max_battery, bank[max_battery_idx + 1 :]


with open("day3.txt", "r") as file:
    for line in file:
        banks.append(line.strip())

for bank in banks:
    batteries = ""

    while len(batteries) < 12:
        battery_to_add, bank_left = find_max_battery(bank, 12 - len(batteries))
        batteries += battery_to_add
        bank = bank_left

    joltages.append(batteries)
    res_two += int(batteries)

print(res_two)
