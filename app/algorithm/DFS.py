import numpy as np
import heapq
from collections import defaultdict, deque

# 872456013
start = np.array(((8, 7, 2), (4, 5, 6), (0, 1, 3)))
# start = np.array(((4, 6, 8), (7, 1, 5), (2, 3, 0)))
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



def check_is_goal(board):
    return np.array_equal(board, goal)


def reconstruct_path(cameFrom, current_sig, visited_count=-1):
    path = []
    while current_sig in cameFrom:
        board = np.frombuffer(current_sig, dtype=np.int64).tolist()
        path.append(board)
        current_sig = cameFrom[current_sig]
    path.reverse()

    return path, {"path_len": len(path), "visited": visited_count}


def DFS(root):
    visited = set()
    node = root
    stack = deque()
    cameFrom = {}
    stack.append(node)

    while stack:
        node = stack.pop()
        node_sig = node.tobytes()
        if node_sig not in visited:
            visited.add(node_sig)
        if check_is_goal(node):
            print("success")
            return reconstruct_path(cameFrom, node_sig, visited_count=len(visited))

        neighbors = get_neighbors(node)

        for neighbor in neighbors:
            neighbor_sig = neighbor.tobytes()
            if neighbor_sig not in visited:
                stack.append(neighbor)
                cameFrom[neighbor_sig] = node_sig

    print("failure")
    return None, None



# Hàm giải + generation data
def reconstruct_path_2(cameFrom, current_sig, visited_count=-1):
    path = []
    while current_sig in cameFrom:
        board = ''.join(map(str, np.frombuffer(current_sig, dtype=np.int64)))
        path.append(board)
        current_sig = cameFrom[current_sig]
    path.reverse()

    # map
    cameFromMap = {}
    for dad_sig, node_sig in cameFrom.items():
        dad_str = ''.join(map(str, np.frombuffer(dad_sig, dtype=np.int64)))
        node_str = ''.join(map(str, np.frombuffer(node_sig, dtype=np.int64)))
        cameFromMap[dad_str] = node_str

    root_str = ''.join(map(str, path[0]))

    return path, {"path_len": len(path), "generated": len(cameFrom), "visited": visited_count, "root": root_str}, cameFromMap


def DFS_2(root):
    visited = set()
    node = root
    stack = deque()
    cameFrom = {}
    stack.append(node)

    while stack:
        node = stack.pop()
        node_sig = node.tobytes()
        if node_sig not in visited:
            visited.add(node_sig)
        if check_is_goal(node):
            print("success")
            return reconstruct_path_2(cameFrom, node_sig, visited_count=len(visited))

        neighbors = get_neighbors(node)

        for neighbor in neighbors:
            neighbor_sig = neighbor.tobytes()
            if neighbor_sig not in visited:
                stack.append(neighbor)
                cameFrom[neighbor_sig] = node_sig
    print("failure")
    return None, None, None



# ===========================
def dfs_and_generation_data(root):
    path, info, dataMap = DFS_2(root)
    # print("info: ", info)
    # print("path: ", path)
    # print("dataMap: ", dataMap)

    with open("./data.txt", "w", encoding="utf-8") as file:
        for key, value in info.items():
            file.write(str(key) + " " + str(value) + "\n")

        file.write("\n")

        for node in path:
            file.write(str(node) + "\n")

        file.write("\n")

        for key, value in dataMap.items():
            file.write(str(key) + " " + str(value) + "\n")

    return path, info, dataMap