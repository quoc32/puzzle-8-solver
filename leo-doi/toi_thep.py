import random
import math
from function import *

def toi_thep(start: str, map: dict, path: list, T_init=100.0, cooling_rate=0.95, T_min=0.01):
    current = start
    current_distance = manhatan_distance(current)
    T = T_init
    solved = False

    while T > T_min and not solved:
        neighbors = get_neighbors(current)
        next_state = random.choice(neighbors)
        next_distance = manhatan_distance(next_state)

        # Nếu chưa thăm thì lưu vào map
        if next_state not in map:
            map[next_state] = (current, next_distance)

        delta = next_distance - current_distance

        # Quyết định có di chuyển hay không
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / T):
            path.append(next_state)
            current = next_state
            current_distance = next_distance

        if current == "123456780":
            solved = True

        T *= cooling_rate  # Làm nguội nhiệt độ

    return solved
