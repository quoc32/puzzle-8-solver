
from tkinter import Tk
import tkinter as tk
import pygame

from Frames.bfs.bfs import create_frame as create_bfs_frame
from Frames.dfs.dfs import create_frame as create_dfs_frame
from Frames.iddfs.iddfs import create_frame as create_ids_frame

# Các hàm tạo frame
create_frame_function = {
        "bfs": create_bfs_frame,
        "dfs": create_dfs_frame,
        "ids": create_ids_frame,
}


# =====================================================
pygame.init()
# Kích thước cửa sổ
WIDTH, HEIGHT = 300, 350
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minh họa Puzzle 8")
# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
# Font chữ
font = pygame.font.Font(None, 36)
# Ma trận 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Kích thước ô vuông
CELL_SIZE = WIDTH // 3
# =====================================================


class App():
    def __init__(self, user=None):
        self.window = Tk()
        self.window.title("Puzzle 8 Solver")
        self.window.geometry("807x457")
        self.window.configure(bg="#ECEAEA")
        self.window.resizable(False, False)

        self.frames = {
            "dfs": create_dfs_frame(self.go_to, self.window, self.update_solver_path),
            "ids": create_ids_frame(self.go_to, self.window, self.update_solver_path),
            "bfs": create_bfs_frame(self.go_to, self.window, self.update_solver_path),
        }
        # 
        self.currentFrame = "bfs"
        self.frames[self.currentFrame].pack(fill="both", expand=True)

        # Loop
        self.window.after(100, self.update_pygame)

        # 
        self.solver_path = [[[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]], [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]]
        self.current_node_index = 1

    def update_pygame(self):
        screen.fill(WHITE)  # Đổ màu nền trắng
        matrix = self.solver_path[self.current_node_index]
        # Vẽ ma trận
        for row in range(3):
            for col in range(3):
                # Tọa độ của ô
                x = col * CELL_SIZE
                y = row * CELL_SIZE

                # Vẽ hình chữ nhật
                pygame.draw.rect(screen, "black", (x, y, CELL_SIZE, CELL_SIZE), 2)

                if matrix[row][col] == 0:
                    pygame.draw.rect(screen, "pink", (x, y, CELL_SIZE, CELL_SIZE))

                # Vẽ số trong ô
                text = font.render(str(matrix[row][col]), True, BLACK)
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                screen.blit(text, text_rect)
        # Vẽ chỉ mục của Node
        text = font.render(str(self.current_node_index), True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2 ,HEIGHT - 20))
        screen.blit(text, text_rect)

        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.current_node_index -= (1 if self.current_node_index > 1 else 0)
                elif event.key == pygame.K_RIGHT:
                    self.current_node_index += (1 if self.current_node_index < (len(self.solver_path) - 1) else 0)

        # Cập nhật màn hình
        pygame.display.flip()

        # Loop
        self.window.after(100, self.update_pygame)


    def go_to(self, frame):
        self.frames[self.currentFrame].pack_forget()
        self.currentFrame = frame    
        self.frames[frame].pack(fill="both", expand=True)

    def update_solver_path(self, path):
        self.current_node_index = 1
        self.solver_path = path

    def turn_on(self):
        self.window.mainloop()


