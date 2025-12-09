def get_adjacent_count(grid, r, c):
    """Count rolls (@) in the 8 adjacent positions."""
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == "@":
                    count += 1
    return count


def find_all_rolls(grid):
    """Return set of all roll coordinates."""
    rolls = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                rolls.add((r, c))
    return rolls


def find_accessible_rolls(grid, rolls):
    """Return set of rolls that can be accessed (fewer than 4 adjacent rolls)."""
    accessible = set()
    for r, c in rolls:
        if get_adjacent_count(grid, r, c) < 4:
            accessible.add((r, c))
    return accessible


def solve():
    # Read input
    with open("day4.txt", "r") as file:
        grid = [list(line.strip()) for line in file]

    # Part 1: Count initially accessible rolls
    all_rolls = find_all_rolls(grid)
    accessible = find_accessible_rolls(grid, all_rolls)
    part1 = len(accessible)

    # Part 2: Simulate iterative removal
    removed_total = 0
    remaining_rolls = all_rolls.copy()

    while True:
        # Find which rolls are currently accessible
        accessible = find_accessible_rolls(grid, remaining_rolls)

        if not accessible:
            break

        # Remove all accessible rolls
        removed_total += len(accessible)
        for r, c in accessible:
            grid[r][c] = "."
            remaining_rolls.remove((r, c))

    part2 = removed_total

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    solve()
