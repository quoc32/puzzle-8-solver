from function import *

def beam_search(start: str, map: dict, path: list, beam_width: int = 2):
    current_states = [start]
    solved = False

    while current_states and not solved:
        print(current_states)
        all_neighbors = []
        for current in current_states:
            neighbors = get_neighbors(current)
            current_distance = manhatan_distance(current)

            for neighbor in neighbors:
                if neighbor not in map:
                    map[neighbor] = (current, manhatan_distance(neighbor))
                    all_neighbors.append(neighbor)
                if neighbor == "123456780":
                    path.append(neighbor)
                    solved = True
                    break

            if solved:
                break
        
        all_neighbors = [x for x in neighbors if manhatan_distance(x) < current_distance]
        if not all_neighbors:
            break

        # Chọn beam_width node có khoảng cách thấp nhất (tốt nhất)
        current_states = sorted(
            all_neighbors, key=lambda x: manhatan_distance(x)
        )[:beam_width]

        # Cập nhật path theo node tốt nhất (tạm thời dùng node đầu tiên để trace)
        for i in current_states:
            path.append(i)

    return solved