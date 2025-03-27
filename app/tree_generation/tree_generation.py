import graphviz
import re

def read_file_as_dict_set_dict(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read().strip()
    
    blocks = re.split(r"\n\s*\n", data)

    if len(blocks) < 3:
        raise ValueError("File không có đủ 3 khối dữ liệu!")

    first_block = {}
    for line in blocks[0].split("\n"):
        parts = line.split()
        if len(parts) == 2:
            key, value = parts
            first_block[key] = int(value) if value.isdigit() else value 

    second_block = set(blocks[1].split("\n")) 

    third_block = {}
    for line in blocks[2].split("\n"):
        parent, child = line.split()
        third_block[parent] = child 

    return first_block, second_block, third_block

def generation():
    # Đọc file
    file_path = "D:\\D\\C\\tri-tue-nhan-tao\\bai-tap-ko-vo-van\\data.txt"
    info_dict, path_set, map_dict = read_file_as_dict_set_dict(file_path)

    # Tạo map nếu số lượng node nhỏ hơn 50000
    if info_dict["generated"] < 50000:

        dot = graphviz.Digraph("bieu_do")

        nodes = set(map_dict.keys()).union(set(map_dict.values()))

        for node in nodes:
            if node in path_set:
                if (node == str(info_dict["root"])) or (node == "123456780"):
                    dot.node(node, style="filled", fillcolor="green")
                    continue
                dot.node(node, style="filled", fillcolor="red")
            else:
                dot.node(node)

        for a, b in map_dict.items():
            if a in path_set and b in path_set:
                dot.edge(b, a, color="red")
            else:
                dot.edge(b, a)

        dot.render("svg_tree_map", format="svg")

    else:
        print("The map too BIG!!! node count: ", info_dict["generated"], "; max: 50_000")
