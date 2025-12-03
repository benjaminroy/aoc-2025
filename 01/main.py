import math
import argparse

INITIAL_NUMBER = 50
LEFT_ROTATION = 'L'
CIRCLE_SIZE = 100

def star_one(rotations, num = INITIAL_NUMBER):
    times_at_zero = 0

    for rot in rotations:
        dir = rot[0]
        dist = int(rot[1:])

        if dir == 'L':
            num = num - dist if num - dist >= 0 else CIRCLE_SIZE + (num - dist)
        else:
            num = num + dist
        
        num %= CIRCLE_SIZE

        if num == 0:
            times_at_zero += 1

    print(times_at_zero)
    return times_at_zero

def star_two(rotations, num = INITIAL_NUMBER):
    times_at_zero = 0

    for rot in rotations:
        dir = rot[0]
        dist = int(rot[1:])

        if dir == LEFT_ROTATION:
            if num > dist:
                num = num - dist
            elif num == dist:
                num = 0
                times_at_zero += 1
            else:
                times_at_zero += math.floor((dist - num) / CIRCLE_SIZE) + (1 if num != 0 else 0)
                num = (num - dist) % CIRCLE_SIZE

        else:
            times_at_zero += math.floor((num + dist) / CIRCLE_SIZE)
            num = (num + dist) % CIRCLE_SIZE

    print(times_at_zero)
    return times_at_zero

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
    rotations = f.read().splitlines()
    f.close()

    star_one(rotations)
    star_two(rotations)
