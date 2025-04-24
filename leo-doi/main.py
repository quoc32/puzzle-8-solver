from leo_doi_don_gian import leo_doi_don_gian
from leo_doi_ngau_nhien import leo_doi_ngau_nhien
from leo_doi_doc_nhat import leo_doi_doc_nhat
from beam_search import beam_search
from toi_thep import toi_thep
from function import *
from gen_map import gen_map
import tkinter as tk

start = "563170824"
path = [start]
map = {start: ("start", manhatan_distance(start))}

def call_leo_doi_don_gian():
    start = input_entry.get()
    if not is_valid_node(start):
        result_label.config(text="Invalid input!")
        return
    path = [start]
    map = {start: ("start", manhatan_distance(start))}
    result = leo_doi_don_gian(start, map, path)
    result_label.config(text=f"Result: {"Solve success!" if result else "Solve failed!"}")
    save_map(map)
    save_path(path)
    gen_map()

def call_leo_doi_ngau_nhien():
    start = input_entry.get()
    if not is_valid_node(start):
        result_label.config(text="Invalid input!")
        return
    path = [start]
    map = {start: ("start", manhatan_distance(start))}
    result = leo_doi_ngau_nhien(start, map, path)
    result_label.config(text=f"Result: {"Solve success!" if result else "Solve failed!"}")
    save_map(map)
    save_path(path)
    gen_map()

def call_leo_doi_doc_nhat():
    start = input_entry.get()
    if not is_valid_node(start):
        result_label.config(text="Invalid input!")
        return
    path = [start]
    map = {start: ("start", manhatan_distance(start))}
    result = leo_doi_doc_nhat(start, map, path)
    result_label.config(text=f"Result: {"Solve success!" if result else "Solve failed!"}")
    save_map(map)
    save_path(path)
    gen_map()

def call_beam_search():
    start = input_entry.get()
    if not is_valid_node(start):
        result_label.config(text="Invalid input!")
        return
    path = [start]
    map = {start: ("start", manhatan_distance(start))}
    result = beam_search(start, map, path)
    result_label.config(text=f"Result: {"Solve success!" if result else "Solve failed!"}")
    save_map(map)
    save_path(path)
    gen_map()

def call_toi_thep():
    start = input_entry.get()
    if not is_valid_node(start):
        result_label.config(text="Invalid input!")
        return
    path = [start]
    map = {start: ("start", manhatan_distance(start))}
    result = toi_thep(start, map, path)
    result_label.config(text=f"Result: {"Solve success!" if result else "Solve failed!"}")
    save_map(map)
    save_path(path)
    gen_map()

def get_random_board(input_entry):
    result_label.config(text="Result: ")
    input_entry.delete(0, tk.END)
    input_entry.insert(0, random_board())

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Leo Đồi")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Nút random board
btn_random = tk.Button(root, text="Random Board", command=lambda : get_random_board(input_entry))
btn_random.pack(pady=10)
# Input cho người dùng nhập chuỗi
input_entry = tk.Entry(root, width=30)
input_entry.pack(pady=10)

# Nút gọi hàm leo_doi_don_gian
btn_don_gian = tk.Button(root, text="Leo Đồi Đơn Giản", command=call_leo_doi_don_gian)
btn_don_gian.pack(pady=10)

# Nút gọi hàm leo_doi_ngau_nhien
btn_ngau_nhien = tk.Button(root, text="Leo Đồi Ngẫu Nhiên", command=call_leo_doi_ngau_nhien)
btn_ngau_nhien.pack(pady=10)

# Nút gọi hàm leo_doi_doc_nhat
btn_doc_nhat = tk.Button(root, text="Leo Đồi Dốc Nhất", command=call_leo_doi_doc_nhat)
btn_doc_nhat.pack(pady=10)

# Nút gọi hàm Beam Search
btn_doc_nhat = tk.Button(root, text="Beam Search", command=call_beam_search)
btn_doc_nhat.pack(pady=10)

# Nút gọi hàm toi_thep
btn_doc_nhat = tk.Button(root, text="Tôi Thép", command=call_toi_thep)
btn_doc_nhat.pack(pady=10)

# Nhãn hiển thị kết quả
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=20)


# Nút xem hình ảnh
import webbrowser
import os
def view():
    try:
        file_path = "output/graph.svg"
        absolute_path = os.path.abspath(file_path)
        webbrowser.open(absolute_path)
    except Exception as e:
        result_label.config(text=f"Error: {e}")
btn_show_image = tk.Button(root, text="Xem Map", command=lambda: view())
btn_show_image.pack(pady=10)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
