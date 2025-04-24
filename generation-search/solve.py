import numpy as np
import random
import copy
from function import *

def solve():
  goal = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]])

  clear_data()

  population_size = 40
  # > Tạo một quần thể ngẫu nhiên ban đầu
  population = generate_population(population_size)
  save_population_to_file(population, "data/data-gen-0.txt")

  i = 0
  while not has_solution(population, goal):
    i += 1
    if i > 1000:
      break  # Important: Giới hạn Số thế hệ 

    # > Cho các cá thể trong quần thể "sinh sản"
    population = get_next_generation(population)

    # > Chọn cá thể tốt nhất từ quần thể
    population = selection(population, goal, population_size)

    print(f"Generation {i}")
    save_population_to_file(population, f"data/data-gen-{i}.txt")


if __name__ == "__main__":
  solve()
