import numpy as np
import random

goal = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 0]])

def manhatan_distance(start, goal):
  distance = 0
  for num in range(1, 9):  # bỏ qua 0 (ô trống)
    x1, y1 = np.argwhere(start == num)[0]
    x2, y2 = np.argwhere(goal == num)[0]
    distance += abs(x1 - x2) + abs(y1 - y2)
  return distance

def generate_population(population_size):
  population = []
  for _ in range(population_size):
    # Tạo một mảng ngẫu nhiên từ 0 đến 8
    individual = np.random.permutation(9).reshape(3, 3)
    population.append(individual)
  return population

def fitness(individual, goal=goal):
  # Tính toán độ thích nghi của cá thể dựa trên khoảng cách Manhattan
  # Để thuận tiện, ta sẽ lấy giá trị âm của khoảng cách để dễ dàng so sánh
  return -manhatan_distance(individual, goal=goal)

def selection(population, goal, population_size):
  # Sắp xếp giảm dần theo fitness (nếu càng cao càng tốt)
  population.sort(key=lambda x: fitness(x, goal), reverse=True)
  
  # Lấy population_size cá thể đầu tiên (tốt nhất)
  selected_population = population[:population_size]
  
  return selected_population


def crossover(parent1, parent2, mutation_rate=0.1):
  pos1 = tuple(np.argwhere(parent1 == 0)[0])
  pos2 = tuple(np.argwhere(parent2 == 0)[0])
  pos = (random.choice([pos1[0], pos2[0]]), random.choice([pos1[1], pos2[1]]))

  f1 = fitness(parent1)
  f2 = fitness(parent2)
  total = f1 + f2

  if total == 0:
    probs = [0.5, 0.5]  # Chia đều nếu không phân biệt được
  else:
    probs = [f1 / total, f2 / total]

  chosen_idx = np.random.choice([0, 1], p=probs)
  chosen_parent = [parent1, parent2][chosen_idx]
  child = np.copy(chosen_parent)

  zero_pos = tuple(np.argwhere(child == 0)[0])
  if pos != zero_pos:
    child[zero_pos], child[pos] = child[pos], child[zero_pos]

  if random.random() < mutation_rate:
    all_positions = [(i, j) for i in range(3) for j in range(3)]
    pos_a, pos_b = random.sample(all_positions, 2)
    child[pos_a], child[pos_b] = child[pos_b], child[pos_a]

  return child




def get_next_generation(population):
  next_generation = []
  population_size = len(population)
  for i in range(population_size):
    parent1 = population[i]
    for j in range(population_size):
      if i == j: continue # > tránh lai giữa cá thể với chính nó
      parent2 = population[j]
      child = crossover(parent1, parent2)
      next_generation.append(child)
  return next_generation

def save_population_to_file(population, filename):
  with open(filename, 'w') as f:
    for individual in population:
      # Flatten rồi chuyển sang chuỗi
      flat_str = ''.join(map(str, individual.flatten()))
      # Thêm độ thích nghi vào chuỗi
      flat_str = flat_str + " " + str(fitness(individual))
      f.write(flat_str + '\n')

def has_solution(population, goal):
  for individual in population:
    if fitness(individual, goal) == 0:
      return True
  return False


# 
import os
def clear_data():
  folder_path = "data"

  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):  # kiểm tra là file (không phải thư mục)
      os.remove(file_path)
def get_num_of_files_in_folder(folder_path):
  return len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
