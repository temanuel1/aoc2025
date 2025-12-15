## Part 1
fresh_ranges = []
produce_to_check = []
res_one = 0

with open("day5.txt", "r") as file:
    for line in file:
        if "-" in line:
            fresh_range = line.strip().split("-")
            fresh_ranges.append((int(fresh_range[0]), int(fresh_range[1])))
        else:
            if line.strip():
                produce_to_check.append(int(line.strip()))

for produce in produce_to_check:
    for start, end in fresh_ranges:
        if produce >= start and produce <= end:
            res_one += 1
            break

print(res_one)

## Part 2
fresh_ranges.sort(key=lambda x: x[0])

# Merge overlapping ranges
merged = []
for start, end in fresh_ranges:
    if merged and start <= merged[-1][1] + 1:
        # Overlaps or adjacent to previous range - extend it
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        # No overlap - add new range
        merged.append((start, end))

# Count total fresh IDs by summing range lengths
res_two = sum(end - start + 1 for start, end in merged)
print(res_two)
