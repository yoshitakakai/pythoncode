import tkinter as tk
import random

# ブロックの種類と形を定義
shapes = [
    [(0, 0), (1, 0), (0, 1), (1, 1)], # 四角
    [(0, 0), (1, 0), (2, 0), (3, 0)], # 直線
    [(0, 0), (0, 1), (1, 1), (2, 1)], # L字
    [(2, 0), (0, 1), (1, 1), (2, 1)], # 反転L字
    [(1, 0), (2, 0), (0, 1), (1, 1)], # Z字
    [(0, 0), (1, 0), (1, 1), (2, 1)], # 反転Z字
    [(0, 0), (1, 0), (2, 0), (1, 1)]  # T字
]

class Block:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

    def rotate_left(self):
        self.shape = [(y, -x) for x, y in self.shape]

    def rotate_right(self):
        self.shape = [(-y, x) for x, y in self.shape]

class Tetris:
    def __init__(self):
        self.width = 10
        self.height = 20
        self.score = 0
        self.board = [[0] * self.width for _ in range(self.height)]
        self.block = None
        self.new_block()
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=200, height=400)
        self.canvas.pack()
        self.draw_board()
        self.root.bind("<Key>", self.key_press)
        self.timer()

    def new_block(self):
        shape = random.choice(shapes)
        self.block = Block(self.width // 2 - 2, 0, shape)

    def move_down(self):
        self.block.y += 1
        if self.check_collision():
            self.block.y -= 1
            self.freeze()

    def move_left(self):
        self.block.x -= 1
        if self.check_collision():
            self.block.x += 1

    def move_right(self):
        self.block.x += 1
        if self.check_collision():
            self.block.x -= 1

    def rotate_left(self):
        self.block.rotate_left()
        if self.check_collision():
            self.block.rotate_right()

    def rotate_right(self):
        self.block.rotate_right()
        if self.check_collision():
            self.block.rotate_left()

    def check_collision(self):
        for x, y in self.block.shape:
            x += self.block.x
            y += self.block.y
            if not(0 <= x < self.width and 0 <= y < self.height) or self.board[y][x]:
                return True
        return False

    def freeze(self):
        for x, y in self.block.shape:
            self.board[y + self.block.y][x + self.block.x] = 1
            self.clear_lines()
            self.new_block()

    def clear_lines(self):
        lines = 0
        for i in range(self.height - 1, -1, -1):
            if 0 not in self.board[i]:
                lines += 1
                for j in range(i, 0, -1):
                    self.board[j] = self.board[j - 1][:]
                    self.board[0] = [0] * self.width
                    self.score += lines ** 2

    def draw_board(self):
        self.canvas.delete("all")
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]:
                    self.canvas.create_rectangle(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill="gray")
                    for x, y in self.block.shape:
                        self.canvas.create_rectangle((x + self.block.x) * 20, (y + self.block.y) * 20, (x + self.block.x) * 20 + 20, (y + self.block.y) * 20 + 20, fill="red")

    def timer(self):
        self.move_down()
        self.draw_board()
        if not self.check_game_over():
            self.root.after(500, self.timer)

    def check_game_over(self):
        if self.check_collision():
            self.canvas.create_text(100, 200, text="Game Over", font=("Helvetica", 36))
            return True
        else:
            return False

    def key_press(self, event):
        key = event.keysym
        if key == "Left":
            self.move_left()
        elif key == "Right":
            self.move_right()
        elif key == "Down":
            self.move_down()
        elif key == "Up":
            self.rotate_left()
        elif key == "space":
            self.rotate_right()
        if name == "main":
            tetris = Tetris()
            tetris.root.mainloop()
