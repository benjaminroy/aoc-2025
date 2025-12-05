import argparse

def get_joltage(banks, num_of_batteries_to_turn_on):
    joltage = 0

    for bank in banks:
        batteries_turned_on = [0] * num_of_batteries_to_turn_on

        for i, digit in enumerate(bank):
            for j, digit2 in enumerate(batteries_turned_on):
                
                if (int(digit) > int(digit2) and i <= len(bank) - (len(batteries_turned_on) - j)):
                    batteries_turned_on[j] = digit
                    for k in range(j + 1, len(batteries_turned_on)):
                        batteries_turned_on[k] = 0
                    break

        joltage += int("".join(batteries_turned_on))

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
