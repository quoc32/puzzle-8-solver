import numpy as np
import heapq
from collections import defaultdict, deque

# 147562308
start = np.array(((1, 4, 7), (5, 6, 2), (3, 0, 8)))
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

# 

def IDS(root, max_depth = 200):
    for depth in range(max_depth + 1):
        result = DLS(root, depth)
        if result:
            return result 

    print("failure")
    return None

def DLS(root, depth_limit):
    visited = set()
    stack = deque([(root, 0)]) 
    cameFrom = {}

    while stack:
        node, depth = stack.pop()
        node_sig = node.tobytes()

        if node_sig not in visited:
            visited.add(node_sig)

        if check_is_goal(node):
            print("success")
            return reconstruct_path(cameFrom, node_sig, visited_count=len(visited))

        if depth < depth_limit:
            neighbors = get_neighbors(node)

            for neighbor in neighbors:
                neighbor_sig = neighbor.tobytes()
                if neighbor_sig not in visited:
                    stack.append((neighbor, depth + 1))
                    cameFrom[neighbor_sig] = node_sig

    return None

    


# Hàm giải + generation data
def reconstruct_path_2(cameFrom, current_sig, visited_count=-1, root_sig=None):
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


    root_str = "None"
    if root_sig:
        root_str = ''.join(map(str, np.frombuffer(root_sig, dtype=np.int64)))

    return path, {"path_len": len(path), "generated": len(cameFrom), "visited": visited_count, "root": root_str}, cameFromMap


def IDS_2(root, max_depth = 2000):
    for depth in range(max_depth + 1):
        result = DLS_2(root, depth)
        if result:
            return result 

    print("failure")
    return None


def DLS_2(root, depth_limit):
    visited = set()
    stack = deque([(root, 0)]) 
    cameFrom = {}

    while stack:
        node, depth = stack.pop()
        node_sig = node.tobytes()

        if node_sig not in visited:
            visited.add(node_sig)

        if check_is_goal(node):
            print("success")
            return reconstruct_path_2(cameFrom, node_sig, visited_count=len(visited), root_sig=root.tobytes())

        if depth < depth_limit:
            neighbors = get_neighbors(node)

            for neighbor in neighbors:
                neighbor_sig = neighbor.tobytes()
                if neighbor_sig not in visited:
                    stack.append((neighbor, depth + 1))
                    cameFrom[neighbor_sig] = node_sig

    return None
    

        
# ===========================
path, info, dataMap = IDS_2(start)
print("info: ", info)
print("path: ", path)
print("dataMap: ", dataMap)

with open("./pygame_demo/data.txt", "w", encoding="utf-8") as file:
    for key, value in info.items():
        file.write(str(key) + " " + str(value) + "\n")

    file.write("\n")

    for node in path:
        file.write(str(node) + "\n")

    file.write("\n")

    for key, value in dataMap.items():
        file.write(str(key) + " " + str(value) + "\n")