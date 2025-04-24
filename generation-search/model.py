import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def load_population_fitness(filename):
    individuals = []
    fitnesses = []

    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                individuals.append(parts[0])
                fitnesses.append(int(parts[1]))
    
    return individuals, fitnesses

# Đọc từ file
filename = "data/data-gen-1.txt"  # ← Đổi thành tên file của bạn
individuals, fitnesses = load_population_fitness(filename)

# Xác định số hàng và cột cho heatmap
cols = 6
rows = int(np.ceil(len(individuals) / cols))

# Tạo lưới dữ liệu cho heatmap (dạng số để tô màu)
fitness_grid = np.full((rows, cols), np.nan)
label_grid = np.full((rows, cols), '', dtype=object)

for idx, (ind, fit) in enumerate(zip(individuals, fitnesses)):
    r, c = divmod(idx, cols)
    fitness_grid[r, c] = fit
    label_grid[r, c] = f"{ind}\n{fit}"

# Vẽ heatmap với nhãn là chuỗi + fitness
plt.figure(figsize=(14, 7))
sns.heatmap(fitness_grid, annot=label_grid, fmt='', cmap="viridis", linewidths=0.5, cbar_kws={"label": "Fitness"})
plt.title("Heatmap quần thể với chuỗi cá thể và fitness")
plt.xlabel("Cột cá thể")
plt.ylabel("Hàng cá thể")
plt.tight_layout()
plt.show()
