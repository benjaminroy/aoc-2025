import argparse
import math

COMMA = ','
NUMBER_OF_SHORTEST_CONNECTIONS = 1000
NUMBER_OF_CIRCUITS = 3

def get_sorted_distances(data):
    distances = []
    visited = set()

    for i, point1 in enumerate(data):
        for j, point2 in enumerate(data):
            if i == j:
                continue

            if (i, j) in visited or (j, i) in visited:
                continue

            x1, y1, z1 = point1.split(COMMA)
            x2, y2, z2 = point2.split(COMMA)
            dist = math.sqrt((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2 + (int(z2) - int(z1)) ** 2)
            distances.append((i, j, dist))
            visited.add((i, j))

    return sorted(distances, key=lambda p: p[2])

def get_largest_circuit_sizes(circuits):
    sizes = [0] * NUMBER_OF_CIRCUITS

    for circuit in circuits:
        for index, size in enumerate(sizes):
            if len(circuit) > size:
                sizes[index] = len(circuit)
                sizes.sort()
                break

    return sizes

def merge_circuits(circuits, id1, id2):
    new_circuit = set([id1, id2])
    merged = []

    for circuit in circuits:
        if circuit & new_circuit:
            new_circuit |= circuit
        else:
            merged.append(circuit)

    merged.append(new_circuit)
    return merged

def star_one(data):
    circuits = []
    distances = get_sorted_distances(data)

    for index in range(NUMBER_OF_SHORTEST_CONNECTIONS):
        id1, id2, _ = distances[index]
        circuits = merge_circuits(circuits, id1, id2)

    result = 1
    for size in get_largest_circuit_sizes(circuits):
        result *= size

    print(result)
    return result
        
def star_two(data):
    circuits = []
    distances = get_sorted_distances(data)
    index = 0

    while True:
        id1, id2, _ = distances[index]
        circuits = merge_circuits(circuits, id1, id2)

        if len(circuits) == 1 and len(circuits[0]) == len(data):
            print(int(data[id1].split(COMMA)[0]) * int(data[id2].split(COMMA)[0]))
            return int(data[id1].split(COMMA)[0]) * int(data[id2].split(COMMA)[0])
        
        index += 1

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
