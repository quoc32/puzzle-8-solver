import numpy as np
import heapq
from collections import defaultdict
import copy
import math

start = np.array(((2, 4, 3), (7, 8, 1), (0, 5, 6)))
goal = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 0)))

def H(board):
    # Manhatan
    return np.sum(np.abs(board - goal))


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


def reconstruct_path(cameFrom, current_sig):
    path = []
    while current_sig in cameFrom:
        board = np.frombuffer(current_sig, dtype=np.int64).tolist()
        path.append(board)
        current_sig = cameFrom[current_sig]
    path.reverse()
    return path

def reconstruct_path(cameFrom, current_sig, info):
    path = []
    while current_sig in cameFrom:
        board = np.frombuffer(current_sig, dtype=np.int64).tolist()
        path.append(board)
        current_sig = cameFrom[current_sig]
    path.reverse()
    return path, info

def IDAStar(start):
    start_sig = start.tobytes()
    bound = H(start)
    path = [start_sig]
    cameFrom = {}
    info = {"depth": 0, "current_explored": 0}
    
    while True:
        t = search(path, 0, bound, cameFrom, info)
        if t == "FOUND":
            return reconstruct_path(cameFrom, path[-1], info)
        if t == math.inf:
            return None
        bound = t
        info[str(info["depth"])] = info["current_explored"]
        info["current_explored"] = 0
        info["depth"] += 1

def search(path, g, bound, cameFrom, info):
    current_sig = path[-1]
    current = np.frombuffer(current_sig, dtype=np.int64).reshape((3, 3))
    f = g + H(current)
    if f > bound:
        return f
    if check_is_goal(current):
        return "FOUND"
    
    min_bound = math.inf
    neighbors = get_neighbors(current)
    info["current_explored"] += len(neighbors)
    
    for neighbor in neighbors:
        neighbor_sig = neighbor.tobytes()
        if neighbor_sig not in path:
            path.append(neighbor_sig)
            cameFrom[neighbor_sig] = current_sig
            t = search(path, g + 1, bound, cameFrom)
            if t == "FOUND":
                return "FOUND"
            if t < min_bound:
                min_bound = t
            path.pop()
    
    return min_bound

def check_is_goal(board):
    return np.array_equal(board, goal)



result = IDAStar(start)
print(result)