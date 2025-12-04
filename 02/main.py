import math
import argparse

def star_one(ranges):
    def is_valid_id(id):
        for i in range(0, math.floor(len(str(id)) / 2)):
            if id[:i + 1] == id[i + 1:]:
                return True
        return False

    result = 0

    for r in ranges[0].split(','):
        r = r.split('-')
        for id in range(int(r[0]), int(r[1]) + 1):
            if is_valid_id(str(id)):
                result += id

    print(result)
    return result

def star_two(ranges):
    def is_valid_id(id):
        for i in range(0, math.floor(len(str(id)) / 2)):
            is_valid = True
            for j in range(1, math.ceil(len(id) / (i + 1))):
                if id[:i + 1] != id[j * (i + 1):(j + 1) * (i + 1)]:
                    is_valid = False
                    break
            if (is_valid):
                return True
        return False

    result = 0

    for r in ranges[0].split(','):
        r = r.split('-')
        for id in range(int(r[0]), int(r[1]) + 1):
            if is_valid_id(str(id)):
                result += id

    print(result)
    return result

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
    ranges = f.read().splitlines()
    f.close()

    star_one(ranges)
    star_two(ranges)
