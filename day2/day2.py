## Part 1
invalids_one = 0


def is_invalid_one(num):
    s = str(num)

    if len(s) % 2 != 0:
        return False

    half = len(s) // 2
    return s[:half] == s[half:]


with open("day2.txt", "r") as file:
    for line in file:
        ranges = line.strip().split(",")
        for r in ranges:
            if not r:
                continue
            start, end = r.split("-")
            start = int(start)
            end = int(end)
            for num in range(start, end + 1):
                if is_invalid_one(num):
                    invalids_one += num

print(invalids_one)


## Part 2
invalids_two = 0


def is_invalid_two(num):
    s = str(num)
    n = len(s)

    for parts in range(2, n + 1):
        if n % parts == 0:
            chunk_size = n // parts
            first_chunk = s[:chunk_size]
            all_equal = True
            for i in range(1, parts):
                if s[i * chunk_size : (i + 1) * chunk_size] != first_chunk:
                    all_equal = False
                    break
            if all_equal:
                return True
    return False


with open("day2.txt", "r") as file:
    for line in file:
        ranges = line.strip().split(",")
        for r in ranges:
            if not r:
                continue
            start, end = r.split("-")
            start = int(start)
            end = int(end)
            for num in range(start, end + 1):
                if is_invalid_two(num):
                    invalids_two += num

print(invalids_two)
