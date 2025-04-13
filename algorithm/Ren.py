import numpy as np
import heapq
from collections import defaultdict, deque
import base64
import random
import math
import numpy as np
from collections import deque

# start = np.array(((3, 6, 0), (4, 8, 2), (1, 7, 5)))
start = np.array(((1, 2, 3), (4, 5, 6), (0, 7, 8)))
goal = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 0)))

def heuristic(board, goal):
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


def check_is_goal(board):
    return np.array_equal(board, goal)

# Hàm giải chay
def reconstruct_path(cameFrom, current_sig, visited_count=-1):
    path = []
    while current_sig in cameFrom:
        board = np.frombuffer(current_sig, dtype=np.int64).tolist()
        path.append(board)
        current_sig = cameFrom[current_sig]
    path.reverse()

    return path, {"path_len": len(path), "visited": visited_count}

def hill_climbing(root, goal):
    current = root
    visited = set()
    cameFrom = {}
    visited.add(current.tobytes())
    
    while True:
        neighbors = get_neighbors(current)
        best_neighbor = None
        best_h = heuristic(current, goal)
        
        for neighbor in neighbors:
            neighbor_sig = neighbor.tobytes()
            if neighbor_sig not in visited:
                h = heuristic(neighbor, goal)
                if h < best_h:  # Chỉ chọn nếu tốt hơn
                    best_h = h
                    best_neighbor = neighbor
        
        if best_neighbor is None or best_h >= heuristic(current, goal):
            break  # Không có bước cải thiện nào nữa
        
        cameFrom[best_neighbor.tobytes()] = current.tobytes()
        visited.add(best_neighbor.tobytes())
        current = best_neighbor
        
        if check_is_goal(current):
            print("Success")
            return reconstruct_path(cameFrom, current.tobytes(), visited_count=len(visited))
    
    print("Failed to reach goal")
    return "fail", "fail"

# Hàm giải + generation data
def reconstruct_path_pygame(cameFrom, current_sig, visited_count=-1):
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

def hill_climbing_pygame(root, goal):
    T = 100000.0
    alpha = 0.995
    current = root
    visited = set()
    cameFrom = {}
    visited.add(current.tobytes())
    
    while True:
        neighbors = get_neighbors(current)
        best_neighbor = None
        best_h = heuristic(current, goal)
        
        for neighbor in neighbors:
            neighbor_sig = neighbor.tobytes()
            if neighbor_sig not in visited:
                h = heuristic(neighbor, goal)
                if h < best_h:  # Chọn nếu tốt hơn
                    best_h = h
                    best_neighbor = neighbor
                # > Nếu nó không lớn hơn chấp nhận nó với xác xuất.
                else:
                    accept = random.random() < math.exp((best_h - h) / T)
                    if accept:
                      best_h = h
                      best_neighbor = neighbor
        
        if best_neighbor is None or best_h >= heuristic(current, goal):
            break  # Không có bước cải thiện nào nữa
        
        cameFrom[best_neighbor.tobytes()] = current.tobytes()
        visited.add(best_neighbor.tobytes())
        current = best_neighbor
        
        if check_is_goal(current):
            print("Success")
            return reconstruct_path_pygame(cameFrom, current.tobytes(), visited_count=len(visited))
        
        T = max(T * alpha, 1e-10) 
    
    print("Failed to reach goal")
    return "fail", "fail", "fail"


# ================
def SHC_and_generation_data(root):
    path, info, dataMap = hill_climbing_pygame(root, goal)
    print("info: ", info)
    print("path: ", path)
    print("dataMap: ", dataMap)

    if info == "fail":
      return

    with open("./pygame_demo/data.txt", "w", encoding="utf-8") as file:
        for key, value in info.items():
            file.write(str(key) + " " + str(value) + "\n")

        file.write("\n")

        for node in path:
            file.write(str(node) + "\n")

        file.write("\n")


        for key, value in dataMap.items():
            file.write(str(key) + " " + str(value) + "\n")

    
    return path, info, dataMap


SHC_and_generation_data(start)
