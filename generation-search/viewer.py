import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# ---------- Load dữ liệu từ file ----------
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

# ---------- Tạo heatmap và lưu vào cache ----------
def create_heatmap_canvas(filename, cols=6):
    individuals, fitnesses = load_population_fitness(filename)

    rows = int(np.ceil(len(individuals) / cols))
    fitness_grid = np.full((rows, cols), np.nan)
    label_grid = np.full((rows, cols), '', dtype=object)

    for idx, (ind, fit) in enumerate(zip(individuals, fitnesses)):
        r, c = divmod(idx, cols)
        fitness_grid[r, c] = fit
        label_grid[r, c] = f"{ind}\n{fit}"

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(fitness_grid, annot=label_grid, fmt='', cmap="magma", linewidths=0.5,
                cbar_kws={"label": "Fitness"}, ax=ax, vmin=-25, vmax=0)
    ax.set_title(f"Heatmap: {os.path.basename(filename)}")
    ax.set_xlabel("Cột cá thể")
    ax.set_ylabel("Hàng cá thể")

    canvas = FigureCanvasTkAgg(fig)
    canvas.draw()
    return canvas

# ---------- Tính trung bình độ thích nghi ----------
def calculate_average_fitness(filename):
    _, fitnesses = load_population_fitness(filename)
    if fitnesses:
        return sum(fitnesses) / len(fitnesses)
    return 0

# ---------- Cập nhật heatmap ----------
def update_heatmap():
    global canvas
    selected = file_list[current_index]
    file_combo.set(selected)

    if canvas:
        canvas.get_tk_widget().pack_forget()

    canvas = cached_canvases[selected]
    canvas.get_tk_widget().master = heatmap_frame
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    avg = calculate_average_fitness(os.path.join("data", selected))
    avg_label.config(text=f"Trung bình Fitness: {avg:.2f}")

# ---------- Callback nút xác nhận ----------
def on_confirm_click():
    global current_index
    selected = file_combo.get()
    if selected in file_list:
        current_index = file_list.index(selected)
        update_heatmap()

# ---------- Callback nút lùi ----------
def on_prev():
    global current_index
    if current_index > 0:
        current_index -= 1
        update_heatmap()

# ---------- Callback nút tiến ----------
def on_next():
    global current_index
    if current_index < len(file_list) - 1:
        current_index += 1
        update_heatmap()

# ---------- Giao diện chính ----------
root = tk.Tk()
root.title("Generation Search Algorithm Viewer")
root.geometry("1000x700")

# Danh sách file
file_list = [f for f in os.listdir("data") if f.endswith(".txt")]
cached_canvases = {}
canvas = None
current_index = 0

# Tiền xử lý heatmap và lưu vào cache
for fname in file_list:
    path = os.path.join("data", fname)
    cached_canvases[fname] = create_heatmap_canvas(path)

# Combobox chọn file
file_combo = ttk.Combobox(root, values=file_list, state="readonly", width=40)
file_combo.pack(pady=10)

# Các nút điều hướng
nav_frame = tk.Frame(root)
nav_frame.pack(pady=5)

prev_btn = ttk.Button(nav_frame, text="<< Lùi", command=on_prev)
prev_btn.pack(side=tk.LEFT, padx=5)

confirm_btn = ttk.Button(nav_frame, text="Xác nhận", command=on_confirm_click)
confirm_btn.pack(side=tk.LEFT, padx=5)

next_btn = ttk.Button(nav_frame, text="Tiến >>", command=on_next)
next_btn.pack(side=tk.LEFT, padx=5)

# Khung chứa heatmap
heatmap_frame = tk.Frame(root)
heatmap_frame.pack(fill=tk.BOTH, expand=True)

# Nhãn hiển thị trung bình độ thích nghi
avg_label = tk.Label(root, text="Trung bình Fitness: N/A", font=("Arial", 12, "bold"))
avg_label.pack(pady=10)

# Hiển thị heatmap mặc định
if file_list:
    file_combo.current(0)
    update_heatmap()

# Đóng cửa sổ đúng cách
def on_close():
    root.destroy()
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
