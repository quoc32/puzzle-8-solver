import numpy as np
import heapq
from collections import defaultdict
import copy

start = np.array(((4, 6, 8), (7, 1, 5), (2, 3, 0)))
# start = np.array(((3, 4, 0), (7, 6, 1), (5, 8, 2)))
goal = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 0)))


def get_neighbors(state):
    neighbors = []
    zero_pos = np.argwhere(state == 0)[0]
    row, col = zero_pos

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < state.shape[0] and 0 <= new_col < state.shape[1]:
            new_state = state.copy()
            new_state[row, col], new_state[new_row, new_col] = new_state[new_row, new_col], new_state[row, col]
            neighbors.append(new_state)

    return neighbors


def reconstruct_path(cameFrom, current_sig, explored_count=-1, frontier_count=-1):
    path = []
    while current_sig in cameFrom:
        board = np.frombuffer(current_sig, dtype=np.int64).tolist()
        path.append(board)
        current_sig = cameFrom[current_sig]
    path.reverse()

    return path, {"path_len": len(path), "explored": explored_count, "frontier": frontier_count}


def check_is_goal(board):
    return np.array_equal(board, goal)


def UCS(root):
    node_sig = root.tobytes()
    
    frontier = []
    heapq.heappush(frontier, (0, node_sig, root))
    frontier_s = {node_sig: 0}

    explored = set()
    cameFrom = {}

    while frontier:
        cost, node_sig, node = heapq.heappop(frontier)
        frontier_s.pop(node_sig, None)
        
        if check_is_goal(node):
            print("Success")
            node_sig = node.tobytes()
            return reconstruct_path(cameFrom, node_sig, explored_count=len(explored), frontier_count=len(frontier))

        explored.add(node_sig)

        neighbors = get_neighbors(node)

        for neighbor in neighbors:
            neighbor_sig = neighbor.tobytes()
            new_cost = cost + 1

            if neighbor_sig not in explored:
                if neighbor_sig not in frontier_s or new_cost < frontier_s[neighbor_sig]:
                    frontier_s[neighbor_sig] = new_cost
                    cameFrom[neighbor_sig] = node_sig
                    heapq.heappush(frontier, (new_cost, neighbor_sig, neighbor))

    print("Failure")
    return [], {"path_len": 0, "explored": len(explored), "frontier": len(frontier)}
        



result = UCS(start)
print(result)