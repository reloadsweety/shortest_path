import csv
# import json
import unittest


class Roadmap(object):
    road_maps = {}
    all_points = set()
    answers = []

    def __init__(self):
        self.initial_data()

    def validate(self, start_node, goal_node):
        if start_node not in self.all_points:
            return (False, 'No have start node in road map')

        if goal_node not in self.all_points:
            return (False, 'No have end node in road map')

        if start_node == goal_node:
            return (False, 'start_node should differenct goal_node')

        return (True, None)

    def initial_data(self):
        with open('path_data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                point_1, point_2, cost = row
                # print(point_1, 'to', point_2, 'is', cost)

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

            # print('All point: ', self.all_points)
            # print('road_map:', json.dumps(self.road_maps, indent=2))

    def shortest_path(self, start, goal, path, cost):
        if start in path:
            return

        path.append(start)
        # print('path', start, path)
        if goal in path:
            self.answers.append({"cost": cost, "path": path})
            # print('answers', {"cost": cost, "path": path})
            return

        for point in self.road_maps[start]:
            if point not in path:
                # print(path, start, '->', point, cost+self.road_maps[start][point])
                self.shortest_path(point, goal, list(path), int(cost + self.road_maps[start][point]))

    def find_shortest_path(self, start_node, goal_node):
        valid, message = self.validate(start_node, goal_node)
        if not valid:
            return message

        # start_node = input("Enter your start_node: ")
        # goal_node = input("Enter your goal_node: ")

        self.shortest_path(start_node, goal_node, [], 0)
        if self.answers:
            print('{} path can go'.format(len(self.answers)))
            for ans in self.answers:
                print(ans)

            answers = sorted(self.answers, key=lambda x: x['cost'])

            return ('Shortest path from {} to {} is {} and have cost {}'.format(
                start_node,
                goal_node,
                " -> ".join(answers[0]['path']),
                answers[0]['cost']))
        else:
            return 'No path found from {} to {}'.format(start_node, goal_node)


if __name__ == '__main__':
    unittest.main()


# shortest_path("A", "G")
# print(answers)

# start_node = input("Enter your start_node: ")
# goal_node = input("Enter your goal_node: ")

# shortest_path(start_node, goal_node, [], 0)
# if answers:
#     print('All path can go')
#     answers = sorted(answers, key=lambda x: x['cost'])
#     for ans in answers:
#         print(ans)

#     print('Shortest path: {} with cost: {}'.format(" -> ".join(answers[0]['path']), answers[0]['cost']))


# print('{} -> {} is '.format(start_node, goal_node))

# Roadmap().find_shortest_path('D', 'F')
