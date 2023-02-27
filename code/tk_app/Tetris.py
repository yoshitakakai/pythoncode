import tkinter as tk
import random

# ブロックの種類と形を定義
SHAPES = [
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
        self.root.bind("<Left>", self.key_press)
        self.root.bind("<Right>", self.key_press)
        self.root.bind("<Down>", self.key_press)
        self.root.bind("<Up>", self.key_press)
        self.root.bind("<space>", self.key_press)
        self.timer()

    def new_block(self):
        shape = random.choice(SHAPES)
        self.block = Block(self.width // 2 - 2, 0, shape)

    def move_down(self):
        self.block.y += 1
        if self.check_collision():
            self.block.y -= 1
            self.freeze()
            self.clear_rows()
            self.new_block()

    def game_over(self):
        for x, y in self.block.shape:
            if self.board[self.block.y + y][self.block.x + x]:
                self.canvas.create_text(100, 200, text="Game Over", font=("Helvetica", 30))
                return True
        return False

    def key_press(self, event):
        if event.keysym == "Left":
            self.move(-1)
        elif event.keysym == "Right":
            self.move(1)
        elif event.keysym == "Down":
            self.move_down()
        elif event.keysym == "Up":
            self.block.rotate_left()
        elif event.keysym == "space":
            self.block.rotate_right()
        self.draw_board()

    def move(self, dx):
        self.block.x += dx
        if self.check_collision():
            self.block.x -= dx

    def check_collision(self):
        for x, y in self.block.shape:
            if not 0 <= self.block.x + x < self.width:
                return True
            if not 0 <= self.block.y + y < self.height:
                return True
            if self.board[self.block.y + y][self.block.x + x]:
                return True
        return False

    def freeze(self):
        for x, y in self.block.shape:
            self.board[self.block.y + y][self.block.x + x] = 1

    def clear_rows(self):
        rows_cleared = 0
        y = self.height - 1
        while y >= 0:
            if all(self.board[y]):
                for i in range(y, 0, -1):
                    self.board[i] = self.board[i - 1][:]
                self.board[0] = [0] * self.width
                rows_cleared += 1
            else:
                y -= 1
        if rows_cleared > 0:
            self.score += rows_cleared ** 2

    def draw_block(self, x, y, shape):
        colors = ["orange", "blue", "red", "green", "purple", "yellow", "cyan"]
        color = colors[SHAPES.index(shape)]
        for i, j in shape:
            self.canvas.create_rectangle((x + j) * 20, (y + i) * 20, (x + j + 1) * 20, (y + i + 1) * 20, fill=color, width=2)

    def draw_board(self):
        self.canvas.delete("all")
        for y, row in enumerate(self.board):
            for x, val in enumerate(row):
                if val:
                    self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="gray", width=2)
        self.draw_block(self.block.x, self.block.y, self.block.shape)

    def timer(self):
        if not self.game_over():
            self.move_down()
            self.draw_board()
            self.root.after(400, self.timer)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    tetris = Tetris()
    tetris.run()

