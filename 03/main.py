import math
import argparse

def get_joltage(banks, number_of_batteries):
    joltage = 0

    for bank in banks:
        batteries = [0] * number_of_batteries

        for i, digit in enumerate(bank):
            for j, battery in enumerate(batteries):
                
                if (int(digit) > int(battery) and i <= len(bank) - (len(batteries) - j)):
                    batteries[j] = digit
                    for k in range(j + 1, len(batteries)):
                        batteries[k] = 0
                    break

        joltage += int("".join(batteries))

    return joltage

def star_one(banks):
    joltage = get_joltage(banks, 2)
    print(joltage)
    return joltage

def star_two(banks):
    joltage = get_joltage(banks, 12)
    print(joltage)
    return joltage

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
    banks = f.read().splitlines()
    f.close()

    star_one(banks)
    star_two(banks)
