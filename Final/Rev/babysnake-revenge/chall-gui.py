import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import tkinter as tk
from tkinter import messagebox

# gampang ni lah aseli ga boong
maze = [
    "##################################################",
    "#...#.........#...#.....#...#.....#.....#.........",
    "###.#.#####.###.#.#.#.###.#.#.#.#.#####.#.#######.",
    "#...#...#...#...#.#.#.#...#...#.#.......#.#...#...",
    "#.#######.###.###.#.#.#.#######.#######.#.#.#.#.#.",
    "#.......#.......#...#...#.....#...#...#.#.#.#.#.#.",
    "#######.#############.#######.###.#.#.###.#.#.#.##",
    "#...#...#.....#.....#.........#...#.#.......#.#...",
    "#.###.###.###.#.###.#########.#.###.#############.",
    "#.....#...#...#.#.#.#.....#...#...#.#.....#.....#.",
    "#.#######.#.###.#.#.#.###.#.#####.#.#.#####.###.#.",
    "#...#.....#.....#...#.#...#...#.#...#.#...#...#.#.",
    "###.###.#########.###.#######.#.#####.#.#.###.#.#.",
    "#.#...#...#...#.#.#.#.........#.......#.#...#.#...",
    "#.###.#.#.#.#.#.#.#.#.#########.#####.#.###.#.####",
    "#.#...#.#...#.#...#.#.#.....#...#.....#...#.#.....",
    "#.#.###.#####.###.#.#.#.###.#####.###.###.#.#####.",
    "#...#.#.#...#...#.#...#.#.........#.....#.#.......",
    "#.###.#.#.#.#.#.#.###.#.###.#########.###.#.#####.",
    "#...#.#.#.#.#.#.#...#.#...#.#.......#.#...#.#...#.",
    "###.#.#.#.#.###.###.#.###.#.#.#####.#.#.#####.#.##",
    "#...#.#.#.#.....#...#.....#.#...#...#.#.......#...",
    "#.###.#.#.#######.#######.#####.#.###.###########.",
    "#...#...#...#.....#...#...#.....#...#.#.......#...",
    "###.#.#####.#.#####.#.#####.#######.###.#####.#.##",
    "#.#.#.#.....#...#...#.#...#...#.......#...#...#...",
    "#.#.###.#######.#.###.#.#.###.#.#####.###.#.#####.",
    "#.#.#...#.......#.#...#.#.#...#.#...#.....#.......",
    "#.#.#.###.#######.#.###.#.#.###.#.#.#############.",
    "#.#.#.#...........#.#...#...#...#.#.#...........#.",
    "#.#.#.#############.###.#########.#.#########.###.",
    "#...#.............#...#...#.......#.#.......#.....",
    "#.###############.###.###.#.#######.#.#####.###.##",
    "#.#.....#.....#...#.#...#.........#.#.#...#...#...",
    "#.#.###.#.###.#.###.###.#######.###.#.###.###.####",
    "#...#...#.#.#...#.....#...#.#...#...#.......#.#...",
    "#####.###.#.#########.###.#.#.###.#########.#.#.#.",
    "#...#.....#.......#...#...#.#...#.........#.#...#.",
    "#.#########.#####.#.#.#.###.###.#####.#####.#####.",
    "#.............#.#...#.#.#.#...#.#...#.......#...#.",
    "#####.#######.#.#.#####.#.#.#.#.#.#.#########.#.#.",
    "#...#.#.....#.#.#.#.....#...#.....#...#...#.#.#...",
    "#.#.###.###.#.#.#.#.###########.#####.#.#.#.#.###.",
    "#.#.....#.....#...#.#.........#.#...#...#...#.#...",
    "#.###.#####.#######.#.###.###.###.#.#####.###.#.##",
    "#.#...#...#.#.......#.#...#.#.#...#...#...#...#.#.",
    "#.#.###.#.###.#########.###.#.#.#####.#.###.###.#.",
    "#.#.#...#...#.#.........#.#...#.#.#...#.#...#...#.",
    "#.###.#####.#.#####.#####.#.###.#.#.#####.###.##..",
    "#.........#.........#...........#.........#......."
]

def genKey(path):
    key = bytearray(16)
    for i, (x, y) in enumerate(path):
        key[i % len(key)] ^= (x + y) % 256
    return bytes(key)

def getFlag(key, iv, ct):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ct), AES.block_size)
    return decrypted.decode('utf-8')

iv = base64.b64decode("mJKl/x5xJ1viL34VEVDI7g==")
ct = base64.b64decode("TbZavV/mHbnC4MYf5R0A46dC7wwE9LG/emivOaehXZhlr5Xd9HqVCIQuHscCV7j4")

class MazeGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maze Game")
        self.geometry("1500x1500")
        
        self.canvas = tk.Canvas(self, width=1300, height=1300, bg="white")
        self.canvas.pack(pady=20)
        
        self.draw_maze()
        
        self.path = []
        
        self.bind("<Button-1>", self.on_click)
        
        self.done_button = tk.Button(self, text="Done", command=self.check_path)
        self.done_button.pack()

    def draw_maze(self):
        self.cell_size = 20
        self.canvas.delete("all")
        for row_index, row in enumerate(maze):
            for col_index, cell in enumerate(row):
                x1 = col_index * self.cell_size
                y1 = row_index * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = "black" if cell == '#' else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def on_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if maze[row][col] == '.':
            self.path.append((row, col))
            self.canvas.create_oval(col * self.cell_size + 5, row * self.cell_size + 5,
                                    col * self.cell_size + self.cell_size - 5, row * self.cell_size + self.cell_size - 5,
                                    fill="red")
        else:
            messagebox.showerror("Invalid Move", "You cannot select this cell.")

    def check_path(self):
        user_key = genKey(self.path)
        if self.validate_path(self.path):
            try:
                flag = getFlag(user_key, iv, ct)
                messagebox.showinfo("Flag", f"Correct path! Decrypted flag: {flag}")
            except (ValueError, IndexError):
                messagebox.showerror("Error", "Failed to decrypt flag. Try a different path.")
        else:
            messagebox.showerror("Invalid Path", "Wrong path! Please try again.")

    def validate_path(self, path):
        for x, y in path:
            if maze[x][y] != '.':
                return False
        return True

if __name__ == "__main__":
    app = MazeGameApp()
    app.mainloop()
