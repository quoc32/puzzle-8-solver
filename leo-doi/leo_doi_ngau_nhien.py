from function import *
import random

def leo_doi_ngau_nhien(current: str, map: dict, path: list):
    solved, canNotSolve = False, False

    while not solved and not canNotSolve:
        neighbors = get_neighbors(current)
        current_distance = manhatan_distance(current)

        for neighbor in neighbors:
            if neighbor not in map:
                map[neighbor] = (current, manhatan_distance(neighbor))

        # Lọc các neighbor tốt hơn
        better_neighbors = [x for x in neighbors if manhatan_distance(x) < current_distance]

        # Chọn ngẫu nhiên 1 thằng trong số đó
        random_better_neighbor = random.choice(better_neighbors or [None])

        print(random_better_neighbor)

        if random_better_neighbor:
            map[random_better_neighbor] = (current, manhatan_distance(random_better_neighbor))
            path.append(random_better_neighbor)
            current = random_better_neighbor
            if random_better_neighbor == "123456780":
                solved = True
        else:
            canNotSolve = True

    return solved




# start = "563170824"

# path = [start]
# map = {
#   start: ("start", manhatan_distance(start)),
# }

# leo_doi_don_gian(start, map, path)

# save_map(map)
# save_path(path)



