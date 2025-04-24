import tkinter as tk
import subprocess
from solve import solve  # Đảm bảo solve.py có hàm solve() không lỗi

def open_heatmap_viewer():
    subprocess.Popen(["python", "viewer.py"])

def run_solve():
    solve()  # Gọi hàm solve khi bấm nút

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Menu Chương trình Tìm kiếm thế hệ")
root.geometry("300x200")

label = tk.Label(root, text="Chọn chức năng", font=("Arial", 14))
label.pack(pady=15)

# Nút mở heatmap
open_btn = tk.Button(root, text="Mở Heatmap Viewer", command=open_heatmap_viewer, width=25)
open_btn.pack(pady=5)

# Nút chạy hàm solve
solve_btn = tk.Button(root, text="Chạy thuật toán (solve)", command=run_solve, width=25)
solve_btn.pack(pady=5)

# Đóng đúng cách
def on_close():
    root.destroy()
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
