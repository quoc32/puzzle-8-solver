from function import *

# >> Hàm giải leo_doi_don_gian
def leo_doi_don_gian(current:str, map:dict, path:list):
  solved, canNotSolve = False, False

  while not solved and not canNotSolve:
    neighbors = get_neighbors(current)
    current_distance = manhatan_distance(current)
    for neighbor in neighbors:
      if neighbor not in map:
        map[neighbor] = (current, manhatan_distance(neighbor))
    first_better_neighbor = next((x for x in neighbors if manhatan_distance(x) < current_distance), None)
    print(first_better_neighbor)
    if first_better_neighbor:
      # Nếu có neighbor tốt hơn thì duyệt tiếp
      map[first_better_neighbor] = (current, manhatan_distance(first_better_neighbor))
      path.append(first_better_neighbor)
      current = first_better_neighbor
      if first_better_neighbor == "123456780":
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



