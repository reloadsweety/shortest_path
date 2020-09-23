import csv
# import json
import unittest


road_maps = {}
all_points = set()

answers = []


with open('path_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        point_1, point_2, cost = row
        # print(point_1, 'to', point_2, 'is', cost)

        if point_1:
            all_points.add(point_1)
        if point_2:
            all_points.add(point_2)

        if point_1 not in road_maps:
            road_maps[point_1] = {}
        road_maps[point_1][point_2] = int(cost) if cost else 0

        if point_2 not in road_maps:
            road_maps[point_2] = {}
        road_maps[point_2][point_1] = int(cost) if cost else 0

    # print('All point: ', all_points)
    # print('road_map:', json.dumps(road_maps, indent=2))
    # print(f'Processed {line_count} lines.')


def shortest_path(start, goal, path=[], cost=0):
    if start in path:
        return

    path.append(start)
    # print('path', start, path)
    if goal in path:
        answers.append({"cost": cost, "path": path})
        # print('answers', {"cost": cost, "path": path})
        return

    for point in road_maps[start]:
        if point not in path:
            # print(path, start, '->', point, cost+road_maps[start][point])
            shortest_path(point, goal, list(path), int(cost+road_maps[start][point]))


# shortest_path("A", "G", [], 0)
# print(answers)

start_node = input("Enter your start_node: ")
goal_node = input("Enter your goal_node: ")


if start_node not in all_points:
    print('No have start node in road map')

if goal_node not in all_points:
    print('No have end node in road map')

if start_node == goal_node:
    print('start_node should differenct goal_node')

shortest_path(start_node, goal_node)
if answers:
    # print('All path can go')
    answers = sorted(answers, key=lambda x: x['cost'])
    # for ans in answers:
    #     print(ans)

    print('Shortest path: {} with cost: {}'.format(" -> ".join(answers[0]['path']), answers[0]['cost']))


# print('{} -> {} is '.format(start_node, goal_node))


class TestShortestPath(unittest.TestCase):
    def setUp(self):
        pass

    def test_start_node_or_goal_node_not_in_road_maps_should_validate_false(self):
        pass

    def test_start_node_or_goal_node_not_in_road_maps_should_validate_false(self):
        pass


# if __name__ == '__main__':
#     unittest.main()
