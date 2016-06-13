# Enter your code here. Read input from STDIN. Print output to STDOUT

from __future__ import print_function
from collections import deque


class Node(object):
    def __init__(self, id, visited=False, distance=-1):
        self.id = id
        self.visited = visited
        self.distance = distance
        self.neighbours = []


def test():
    n_nodes, n_edges = (int(number) for number in raw_input().strip().split())

    nodes = {}
    # Add all nodes in order
    for id in range(n_nodes):
        nodes[id+1] = Node(id+1)

    # Add edges
    for _ in range(n_edges):
        start_id, end_id = (int(number) for number in raw_input().strip().split())
        nodes[start_id].neighbours.append(nodes[end_id])
        nodes[end_id].neighbours.append(nodes[start_id])

    # Start from node
    start_node = nodes[input()]
    start_node.distance = 0
    start_node.visited = True
    queue = deque()
    queue.append(start_node)

    while queue:
        head = queue.popleft()
        for node in head.neighbours:
            if not node.visited:
                node.visited = True
                node.distance = head.distance + 6
                queue.append(node)

    for i in range(1, n_nodes + 1):
        distance = str(nodes[i].distance)
        if distance != '0':
            print(distance, end=' ', sep='')

    print('', end='\n')


def main():
    total = input()
    for _ in range(total):
        test()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
