import argparse
import itertools
from tqdm import tqdm

COMMA = ','

def star_one(data):
    area = 0

    for combination in tqdm(list(itertools.product(data, data))):
        x1, y1 = map(int, combination[0].split(COMMA))
        x2, y2 = map(int, combination[1].split(COMMA))
        area = max((int(y2) - int(y1) + 1) * (int(x2) - int(x1) + 1), area)

    print(area)
    return area

def get_perimeter_coords(data):
    x_coords_by_row = {}
    y_coords_by_col = {}

    for index, p1 in enumerate(data):
        p2 = data[(index + 1) % len(data)]
        x1, y1 = map(int, p1.split(COMMA))
        x2, y2 = map(int, p2.split(COMMA))

        if x1 != x2 and y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                x_coords_by_row.setdefault(y1, set()).add(x)
                y_coords_by_col.setdefault(x, set()).add(y1)

        elif y1 != y2 and x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                y_coords_by_col.setdefault(x1, set()).add(y)
                x_coords_by_row.setdefault(y, set()).add(x1)

    return x_coords_by_row, y_coords_by_col

def get_rect_perimeter_points(x1, y1, x2, y2):
    points = []

    for y in range(min(y1, y2), max(y1, y2) + 1):
        points.append((x1, y))
        points.append((x2, y))

    for x in range(min(x1, x2) + 1, max(x1, x2)):
        points.append((x, y1))
        points.append((x, y2))

    return points

def is_rect_fully_inside_loop(rect_perimeter_points, min_x_for_y, max_x_for_y, min_y_for_x, max_y_for_x, x_coords_by_row, y_coords_by_col):
    for x, y in rect_perimeter_points:
        if y not in min_x_for_y:
            min_x_for_y[y] = min(x_coords_by_row[y])

        if y not in max_x_for_y:
            max_x_for_y[y] = max(x_coords_by_row[y])

        if x not in min_y_for_x:
            min_y_for_x[x] = min(y_coords_by_col[x])

        if x not in max_y_for_x:
            max_y_for_x[x] = max(y_coords_by_col[x])

        if (y not in x_coords_by_row or x < min_x_for_y[y] or x > max_x_for_y[y]):
            return False

        if (x not in y_coords_by_col or y < min_y_for_x[x] or y > max_y_for_x[x]):
            return False

    return True

def star_two(data):
    max_area = 0
    min_x_for_y = {}
    max_x_for_y = {}
    min_y_for_x = {}
    max_y_for_x = {}
    x_coords_by_row, y_coords_by_col = get_perimeter_coords(data)

    for combination in tqdm(list(itertools.product(data, data))):
        x1, y1 = map(int, combination[0].split(COMMA))
        x2, y2 = map(int, combination[1].split(COMMA))

        area = (abs(int(y2) - int(y1)) + 1) * (abs((int(x2) - int(x1)) + 1))

        if area < max_area:
            continue

        if ((x1 not in x_coords_by_row[y2] or y2 not in y_coords_by_col[x1])
            and (x2 not in x_coords_by_row[y1] or y1 not in y_coords_by_col[x2])
        ):
            continue  # 3rd corner is missing

        rect_perimeter_points = get_rect_perimeter_points(x1, y1, x2, y2)

        if is_rect_fully_inside_loop(
            rect_perimeter_points,
            min_x_for_y,
            max_x_for_y,
            min_y_for_x,
            max_y_for_x,
            x_coords_by_row,
            y_coords_by_col
        ):
            max_area = area

    print(max_area)
    return max_area

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

    star_one(data)
    star_two(data)
