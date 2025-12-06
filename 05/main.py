import argparse

def merge_ranges(ranges):
    index1 = 0

    while index1 < len(ranges):
        found = False
        range1 = ranges[index1]
        min_range1 = int(range1.split('-')[0])
        max_range1 = int(range1.split('-')[1])

        for index2, range2 in enumerate(ranges):
            if index1 == index2:
                continue

            min_range2 = int(range2.split('-')[0])
            max_range2 = int(range2.split('-')[1])

            if (max_range2 >= max_range1 and min_range2 <= max_range1) or (max_range2 >= min_range1 and min_range2 <= min_range1):
                ranges[index1] = f"{min([min_range1, min_range2])}-{max([max_range1, max_range2])}"
                ranges.pop(index2)
                found = True
                break

        if found == False:
            index1 += 1

    return ranges

def star_one(ranges, ingredients):
    number_of_ingredients = 0

    for ingredient in ingredients:
        for r in ranges:
            min_id = int(r.split('-')[0])
            max_id = int(r.split('-')[1])

            if int(ingredient) >= min_id and int(ingredient) <= max_id:
                number_of_ingredients += 1
                break

    print(number_of_ingredients)
    return number_of_ingredients

def star_two(ranges):
    number_of_ids = 0
    ranges = merge_ranges(ranges)

    for r in ranges:
        min_id = int(r.split('-')[0])
        max_id = int(r.split('-')[1])
        number_of_ids += max_id - min_id + 1

    print(number_of_ids)
    return number_of_ids

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
    data = f.read().split('\n\n')
    ranges = data[0].splitlines()
    ingredients = data[1].splitlines()
    f.close()

    star_one(ranges, ingredients)
    star_two(ranges)
