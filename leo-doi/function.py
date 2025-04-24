import numpy as np
import random

goal = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 0]])

def manhatan_distance(start:str, goal=goal):
  distance = 0
  start_arr = np.array(list(start), dtype=int).reshape((3, 3))
  for num in range(1, 9):  # bỏ qua 0 (ô trống)
    x1, y1 = np.argwhere(start_arr == num)[0]
    x2, y2 = np.argwhere(goal == num)[0]
    distance += abs(x1 - x2) + abs(y1 - y2)
  return distance

def is_valid_node(node:str):
  return len(node) == 9 and set(node) == set("012345678")

def get_neighbors(node):
  # if not is_valid_node(node):
  #   print("Chuỗi node không hợp lệ")
  #   return
  neighbors = []
  zero_index = node.index('0')

  # Các hướng và điều kiện
  moves = {
      'left':  -1 if zero_index % 3 != 0 else None,
      'right': +1 if zero_index % 3 != 2 else None,
      'up':    -3 if zero_index >= 3 else None,
      'down':  +3 if zero_index <= 5 else None,
  }

  for move, offset in moves.items():
      if offset is not None:
          new_index = zero_index + offset
          # Hoán đổi vị trí
          new_node = list(node)
          new_node[zero_index], new_node[new_index] = new_node[new_index], new_node[zero_index]
          neighbors.append("".join(new_node))

  return neighbors

def save_map(map: dict, filename="data/map.txt"):
    with open(filename, "w") as f:
        for key, (val1, val2) in map.items():
            f.write(f"{key} {val1} {val2}\n")
            
def save_path(arr:list, filename="data/path.txt"):
    with open(filename, "w") as f:
        f.write(" ".join(arr) + "\n")

def random_board():
    # Tạo chuỗi ngẫu nhiên gồm các số từ 0-8
    numbers = list("012345678")
    random.shuffle(numbers)
    return "".join(numbers)

def check_success():
  path = []
  with open('data/path.txt', 'r') as f:
    line = f.readline()
    path = line.strip().split() 
  print(path)
  return path[-1] == "123456780"