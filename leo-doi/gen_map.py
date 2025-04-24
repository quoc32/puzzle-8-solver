from graphviz import Digraph

def gen_map():
    dot = Digraph(comment='Ví dụ đồ thị')
    path = []
    with open('data/path.txt', 'r') as f:
        line = f.readline()
        path = line.strip().split() 

    with open('data/map.txt', 'r') as file:
        for line in file:
            node, parent, dis = line.split()
            if parent == "start":
                dot.node(node, shape='box', color='red', label=f'{node}({dis})')
                continue

            if node == path[-1]:
                dot.node(node, shape='box', color='red', label=f'{node}({dis})')
            else:
                dot.node(node, label=f'{node}({dis})')

            if dis == "0":
                dot.node(node, shape='box', color='green', label=f'{node}(goal)')
                
            dot.edge(parent, node, color=("orange" if (parent in path and node in path) else "black"))
            

    # Xuất ra file và hiển thị
    dot.render('output/graph', format='svg', view=False)
