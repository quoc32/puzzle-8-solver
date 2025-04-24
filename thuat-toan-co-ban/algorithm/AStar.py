import numpy as np
import heapq
from collections import defaultdict
import copy

start = np.array(((2, 4, 3), (7, 8, 1), (0, 5, 6)))
goal = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 0)))

def H(board):
    # Manhatan
    return np.sum(np.abs(board - goal))


def check_is_goal(board):
    return np.array_equal(board, goal)

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

def AStar(start):
    start_sig = start.tobytes()

    openSet = []
    heapq.heappush(openSet, (0, start_sig, start))
    openSet_s = {start_sig}

    cameFrom = {}

    gScore = defaultdict(lambda: float('inf'))
    gScore[start_sig] = 0
    
    fScore = defaultdict(lambda: float('inf'))
    fScore[start_sig] = H(start)

    while openSet:
        _, current_sig, current = heapq.heappop(openSet)

        openSet_s.remove(current_sig)

        if check_is_goal(current):
            print("success")
            return reconstruct_path(cameFrom, current_sig)

        neighbors = get_neighbors(current)

        for neighbor in neighbors:
            neighbor_sig = neighbor.tobytes()
            tentative_gScore = gScore[current_sig] + 1

            if tentative_gScore < gScore[neighbor_sig]:
                cameFrom[neighbor_sig] = current_sig
                gScore[neighbor_sig] = tentative_gScore
                fScore[neighbor_sig] = tentative_gScore + H(neighbor)

                if neighbor_sig not in openSet_s:
                    heapq.heappush(openSet, (fScore[neighbor_sig], neighbor_sig, neighbor))
                    openSet_s.add(neighbor_sig)

    print("failure")
    return None
        


# Hàm giải + generation data
def reconstruct_path_2(cameFrom, current_sig, visited_count=-1, root_sig=None):
    path = []
    while current_sig in cameFrom:
        board = ''.join(map(str, np.frombuffer(current_sig, dtype=np.int64)))
        path.append(board)
        current_sig = cameFrom[current_sig]

    root_str = ''.join(map(str, np.frombuffer(root_sig, dtype=np.int64)))
    path.append(root_str)
    path.reverse()

    # map
    cameFromMap = {}
    for dad_sig, node_sig in cameFrom.items():
        dad_str = ''.join(map(str, np.frombuffer(dad_sig, dtype=np.int64)))
        node_str = ''.join(map(str, np.frombuffer(node_sig, dtype=np.int64)))
        cameFromMap[dad_str] = node_str

    
    return path, {"path_len": len(path), "generated": len(cameFrom), "visited": visited_count, "root": root_str}, cameFromMap

def AStar_2(start):
    visited_count = 0
    start_sig = start.tobytes()

    openSet = []
    heapq.heappush(openSet, (0, start_sig, start))
    openSet_s = {start_sig}

    cameFrom = {}

    gScore = defaultdict(lambda: float('inf'))
    gScore[start_sig] = 0
    
    fScore = defaultdict(lambda: float('inf'))
    fScore[start_sig] = H(start)

    while openSet:
        visited_count += 1
        _, current_sig, current = heapq.heappop(openSet)

        openSet_s.remove(current_sig)

        if check_is_goal(current):
            print("success")
            return reconstruct_path_2(cameFrom, current_sig, visited_count=visited_count, root_sig=start_sig)

        neighbors = get_neighbors(current)

        for neighbor in neighbors:
            neighbor_sig = neighbor.tobytes()
            tentative_gScore = gScore[current_sig] + 1

            if tentative_gScore < gScore[neighbor_sig]:
                cameFrom[neighbor_sig] = current_sig
                gScore[neighbor_sig] = tentative_gScore
                fScore[neighbor_sig] = tentative_gScore + H(neighbor)

                if neighbor_sig not in openSet_s:
                    heapq.heappush(openSet, (fScore[neighbor_sig], neighbor_sig, neighbor))
                    openSet_s.add(neighbor_sig)

    print("failure")
    return None

# =======================
path, info, dataMap = AStar_2(start)
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