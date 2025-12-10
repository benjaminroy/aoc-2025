from main import connect_boxes, get_circuits, get_dist_between_boxes
import math

class TestDayEight:
    def test_connect_boxes(self):
        network = connect_boxes({}, 1, 2)
        assert 1 in network
        assert 2 in network[1]
        assert 2 in network
        assert 1 in network[2]

        network = connect_boxes({1: [3]}, 1, 2)
        assert 1 in network
        assert 2 in network[1]
        assert 3 in network[1]
        assert 2 in network
        assert 1 in network[2]

    def test_get_circuits(self):
        network = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
        circuits = get_circuits(network)
        assert [{0, 1, 2, 3}] == circuits

    def test_get_distance_between_points(self):
        dist = get_dist_between_boxes([1,1,1], [1,1,2])
        assert dist == 1

        dist = get_dist_between_boxes([1,1,1], [2,2,2])
        assert dist == math.sqrt(3)
