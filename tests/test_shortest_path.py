import unittest

from ..shortest_path import Roadmap


class TestShortestPath(unittest.TestCase):
    def setUp(self):
        self.road_map = Roadmap("path_data.csv")
        self.road_map.answers = []

    def test_start_node_or_goal_node_not_in_road_maps_should_validate_false(self):
        expect = self.road_map.find_shortest_path('Z', 'A')
        self.assertEqual(expect, 'No have start node in road map')

        expect = self.road_map.find_shortest_path('A', 'Z')
        self.assertEqual(expect, 'No have end node in road map')

    def test_start_node_same_goal_node_not_in_road_maps_should_validate_false(self):
        expect = self.road_map.find_shortest_path('A', 'A')
        self.assertEqual(expect, 'start_node should differenct goal_node')

    def test_shortest_path_with_start_point_A_and_goal_point_G_should_return_correctly_data(self):
        expect = self.road_map.find_shortest_path('A', 'G')
        self.assertEqual(expect, 'Shortest path from A to G is A -> D -> G and have cost 9')

    def test_shortest_path_with_start_point_B_and_goal_point_C_should_return_correctly_data(self):
        expect = self.road_map.find_shortest_path('B', 'C')
        self.assertEqual(expect, 'Shortest path from B to C is B -> C and have cost 4')

    def test_shortest_path_with_start_point_D_and_goal_point_F_should_return_correctly_data(self):
        expect = self.road_map.find_shortest_path('D', 'F')
        self.assertEqual(expect, 'Shortest path from D to F is D -> A -> E -> F and have cost 13')

    def test_shortest_path_with_start_point_H_and_goal_point_D_should_return_correctly_data(self):
        expect = self.road_map.find_shortest_path('G', 'E')
        self.assertEqual(expect, 'Shortest path from G to E is G -> D -> A -> E and have cost 13')

    def test_shortest_path_with_no_answer_exist_should_return_correctly_data(self):
        expect = self.road_map.find_shortest_path('A', 'I')
        self.assertEqual(expect, 'No path found from A to I')


if __name__ == '__main__':
    unittest.main()