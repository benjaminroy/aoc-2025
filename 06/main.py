
import argparse

def star_one(data, operators):
    equations = []
    result = 0

    for line in data:
        line = line.split()
        for index, number in enumerate(line):
            if index == len(equations):
                equations.append(number)
            else:
                equations[index] += operators[index] + number

    for eq in equations:
        result += eval(eq)

    print(result)
    return result

def star_two(data, operators):
    equations = []
    result = 0
    transposed_data = []

    for i, line in enumerate(data):
        for j in range(len(line)):
            if j not in transposed_data:
                transposed_data.append("")
            if data[i][j] != ' ':
                transposed_data[j] += data[i][j]

    i = 0
    for line in transposed_data:
        number = "".join(line).strip()
        if number == '':
            i += 1
        else:
            if i == len(equations):
                equations.append(number)
            else:
                equations[i] += operators[i] + number

    for eq in equations:
        result += eval(eq)

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
    data = f.read().splitlines()
    f.close()

    star_one(data[:-1], data[-1].split())
    star_two(data[:-1], data[-1].split())
