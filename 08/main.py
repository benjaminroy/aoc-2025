
import argparse
import math

COMMA = ','
NUMBER_OF_SHORTEST_CONNECTIONS = 1000
NUMBER_OF_CIRCUITS = 3

def build_network(data):
    distances = get_distances(data)
    number_of_connections = 0
    network = {}

    while number_of_connections < NUMBER_OF_SHORTEST_CONNECTIONS:
        id1, id2, _ = distances[number_of_connections]
        if id2 not in network.get(id1, []):
            connect_boxes(network, id1, id2)
            number_of_connections += 1

    return network

def connect_boxes(network, id1, id2):
    network[id1] = [id2] if id1 not in network else network[id1] + [id2]
    network[id2] = [id1] if id2 not in network else network[id2] + [id1]
    return network

def get_circuits(network, circuits = []):
    for node_id, node_ids in network.items():
        new_circuit = set([node_id] + node_ids)
        merged = []

        for circuit in circuits:
            if circuit & new_circuit:
                new_circuit |= circuit
            else:
                merged.append(circuit)

        merged.append(new_circuit)
        circuits = merged

    return circuits

def get_dist_between_boxes(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2 + (int(z2) - int(z1)) ** 2)

def get_distances(data):
    distances = []
    visited = set()

    for i, point1 in enumerate(data):
        for j, point2 in enumerate(data):
            if i == j:
                continue

            if (i, j) in visited or (j, i) in visited:
                continue

            dist = get_dist_between_boxes(point1.split(COMMA), point2.split(COMMA))
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

def star_one(data):
    network = build_network(data)
    circuits = get_circuits(network)

    result = 1
    for size in get_largest_circuit_sizes(circuits):
        result *= size

    print(result)
    return result
        
def star_two(data):
    circuits = []
    distances = get_distances(data)
    number_of_connections = 0
    network = {}

    while True:
        id1, id2, _ = distances[number_of_connections]
        if id2 not in network.get(id1, []):
            connect_boxes(network, id1, id2)
            circuits = get_circuits(network, circuits)
            if len(circuits) == 1 and len(circuits[0]) == len(data):
                print(int(data[id1].split(COMMA)[0]) * int(data[id2].split(COMMA)[0]))
                return
            number_of_connections += 1

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
