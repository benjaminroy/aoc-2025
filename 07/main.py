
import argparse

EMPTY_SPACE = "."
SPLITTER = "^"
STARTING_POINT = "S"
  
def star_one(grid):
    split_count = 0

    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if (cell == STARTING_POINT or cell == "|") and y + 1 < len(grid):
                if grid[y + 1][x] == EMPTY_SPACE:
                    grid[y + 1] = grid[y + 1][:x] + "|" + grid[y + 1][x + 1:]
                elif grid[y + 1][x] == SPLITTER:
                    split_count += 1
                    if x - 1 >= 0:
                        grid[y + 1] = grid[y + 1][:x - 1] + "|" + grid[y + 1][x:]
                    if x + 1 < len(line):
                        grid[y + 1] = grid[y + 1][:x + 1] + "|" + grid[y + 1][x + 2:]

    print(split_count)
    return split_count

def star_two(grid):
    grid = [list(line) for line in grid[::-1]]

    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if grid[y - 1][x] == SPLITTER:
                grid[y][x] = f"{int(grid[y - 1][x - 1]) + int(grid[y - 1][x + 1])}"
            elif cell == EMPTY_SPACE:
                grid[y][x] = '1' if y == 0 else grid[y - 1][x]
            elif cell == STARTING_POINT:
                print(grid[y - 1][x])
                # print(grid)
                return grid[y - 1][x]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="2025/01")
    parser.add_argument(
        "--test", "-t",
        action="store_true",
        help="Use test input file"
    )
    args = parser.parse_args()

    filename = "input-test.txt" if args.test else "input.txt"
    f = open(filename, "r")
    data = f.read().splitlines()
    f.close()

    star_one(data.copy())
    star_two(data.copy())
