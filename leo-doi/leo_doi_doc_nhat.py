from function import *
import random

# >> Hàm giải leo_doi_don_gian
def leo_doi_doc_nhat(current:str, map:dict, path:list):
  solved, canNotSolve = False, False

  while not solved and not canNotSolve:
    neighbors = get_neighbors(current)
    current_distance = manhatan_distance(current)
    for neighbor in neighbors:
      if neighbor not in map:
        map[neighbor] = (current, manhatan_distance(neighbor))
    first_best_neighbor = min(neighbors, key=lambda x: manhatan_distance(x))
    if manhatan_distance(first_best_neighbor) > current_distance:
      first_best_neighbor = None
    print(first_best_neighbor)
    if first_best_neighbor:
      # Nếu có neighbor tốt hơn thì duyệt tiếp
      map[first_best_neighbor] = (current, manhatan_distance(first_best_neighbor))
      path.append(first_best_neighbor)
      current = first_best_neighbor
      if first_best_neighbor == "123456780":
        solved = True
    else:
      canNotSolve = True

  return True if solved else False




# start = "563170824"

# path = [start]
# map = {
#   start: ("start", manhatan_distance(start)),
# }

# leo_doi_don_gian(start, map, path)

# save_map(map)
# save_path(path)



