import csv
# import json
import unittest


class Roadmap(object):
    road_maps = {}
    all_points = set()
    answers = []

    def __init__(self, file_name):
        self.initial_data(file_name)

    def validate(self, start_node, goal_node):
        if start_node not in self.all_points:
            return (False, 'No have start node in road map')

        if goal_node not in self.all_points:
            return (False, 'No have end node in road map')

        if start_node == goal_node:
            return (False, 'start_node should differenct goal_node')

        return (True, None)

    def initial_data(self, file_name):
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                point_1, point_2, cost = row

                if point_1:
                    self.all_points.add(point_1)
                if point_2:
                    self.all_points.add(point_2)

                if point_1 not in self.road_maps:
                    self.road_maps[point_1] = {}
                self.road_maps[point_1][point_2] = int(cost) if cost else 0

                if point_2 not in self.road_maps:
                    self.road_maps[point_2] = {}
                self.road_maps[point_2][point_1] = int(cost) if cost else 0

    def shortest_path(self, start, goal, path, cost):
        if start in path:
            return

        path.append(start)
        if goal in path:
            self.answers.append({"cost": cost, "path": path})
            return

        for point in self.road_maps[start]:
            if point not in path:
                self.shortest_path(point, goal, list(path), int(cost + self.road_maps[start][point]))

    def find_shortest_path(self, start_node, goal_node):
        valid, message = self.validate(start_node, goal_node)
        if not valid:
            return message

        self.shortest_path(start_node, goal_node, [], 0)
        if self.answers:


            answers = sorted(self.answers, key=lambda x: x['cost'])

            return ('Shortest path from {} to {} is {} and have cost {}'.format(
                start_node,
                goal_node,
                " -> ".join(answers[0]['path']),
                answers[0]['cost']))
        else:
            return 'No path found from {} to {}'.format(start_node, goal_node)


if __name__ == '__main__':
    file_name = input("Enter your file name: ")
    start_node = input("Enter your start_node: ")
    goal_node = input("Enter your goal_node: ")

    road_map = Roadmap(file_name)
    print(road_map.find_shortest_path(start_node, goal_node))