import solve_puz8_module as solver
import time



print("Solve with bfs:")
start_time = time.perf_counter()
print(solver.solve_with_bfs(0, 1, 3, 2, 4, 5, 6, 8, 7))
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("BFS finish with", elapsed_time, "ms")


print("==============================")


start_time = time.perf_counter()
print("Solve with iddfs:")
print(solver.solve_with_iddfs(0, 1, 3, 2, 4, 5, 6, 8, 7))
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("DFS finish with", elapsed_time, "ms")


print("==============================")


start_time = time.perf_counter()
print("Solve with dfs:")
print(solver.solve_with_dfs(0, 1, 3, 2, 4, 5, 6, 8, 7))
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("DFS finish with", elapsed_time, "ms")