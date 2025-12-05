import argparse

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (1, 1),
    (1, -1),
    (-1, 0),
    (-1, 1),
    (-1, -1),
]
EMPTY_SPACE = '.'
MAX_ADJACENT_ROLLS = 3
ROLL_OF_PAPERS = '@'

def get_accessible_rolls(grid):
    accessible_rolls = []

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != ROLL_OF_PAPERS:
                continue

            k = 0
            for dir in DIRECTIONS:
                if (
                    i + dir[0] >= 0 and i + dir[0] < len(grid) and
                    j + dir[1] >= 0 and j + dir[1] < len(row) and
                    grid[i + dir[0]][j + dir[1]] == ROLL_OF_PAPERS
                ):
                    k += 1
                
                    if (k > MAX_ADJACENT_ROLLS):
                        pass
            
            if k <= MAX_ADJACENT_ROLLS:
                accessible_rolls.append((i, j))
    
    return accessible_rolls                          

def remove_rolls(grid, num_removed_rolls):
    accessible_rolls = get_accessible_rolls(grid)

    if (len(accessible_rolls) == 0):
        return num_removed_rolls

    for i, j in accessible_rolls:
        grid[i] = grid[i][:j] + EMPTY_SPACE + grid[i][j + 1:]

    num_removed_rolls += len(accessible_rolls)

    return remove_rolls(grid, num_removed_rolls)

def star_one(grid):
    accessible_rolls = get_accessible_rolls(grid)
    number_of_accessibled_rolls = len(accessible_rolls)
    print(number_of_accessibled_rolls)
    return number_of_accessibled_rolls  

def star_two(grid):
    num_removed_rolls = remove_rolls(grid, 0)
    print(num_removed_rolls)
    return num_removed_rolls

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
    grid = f.read().splitlines()
    f.close()

    star_one(grid)
    star_two(grid)
