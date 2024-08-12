import numpy as np
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

# Maze generator using DFS
def generate_maze(size):
    maze = np.ones((size, size), dtype=int)  # 1 represents walls
    stack = [(1, 1)]
    maze[1, 1] = 0  # 0 represents paths
    path = [(1, 1)]  # Store the path taken

    while stack:
        x, y = stack[-1]
        stack.pop()
        neighbors = []
        for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
            nx, ny = x + dx, y + dy
            if 1 <= nx < size - 1 and 1 <= ny < size - 1 and maze[nx, ny] == 1:
                if dx == 2 and maze[x + 1, y] == 1:
                    neighbors.append((nx, ny))
                elif dx == -2 and maze[x - 1, y] == 1:
                    neighbors.append((nx, ny))
                elif dy == 2 and maze[x, y + 1] == 1:
                    neighbors.append((nx, ny))
                elif dy == -2 and maze[x, y - 1] == 1:
                    neighbors.append((nx, ny))

        if neighbors:
            stack.append((x, y))
            nx, ny = random.choice(neighbors)
            maze[nx, ny] = 0
            maze[x + (nx - x) // 2, y + (ny - y) // 2] = 0
            stack.append((nx, ny))
            path.append((nx, ny))  # Add the new path point

    return maze, path

def print_maze(maze, path=None):
    if path is None:
        path = []
    size = maze.shape[0]
    for i in range(size):
        row = []
        for j in range(size):
            if (i, j) in path:
                row.append('*')  # Mark the path taken
            elif maze[i, j] == 1:
                row.append('#')
            else:
                row.append('.')
        print(''.join(row))
    print()

def maze_to_key(maze, path):
    key = bytearray()
    size = maze.shape[0]
    for (i, j) in path:
        key.append(i * size + j)
    return bytes(key.ljust(16, b'\0')[:16])  # Ensure the key is exactly 16 bytes long

def encrypt_flag(flag, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(flag.encode(), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return iv, ct

def decrypt_flag(iv, ct, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=b64decode(iv))
    pt = unpad(cipher.decrypt(b64decode(ct)), AES.block_size).decode('utf-8')
    return pt

# Generate a 30x30 maze and get the path
maze_size = 30
maze, path = generate_maze(maze_size)

# Print the original maze
print("Original Maze:")
print_maze(maze)

# Print the maze with the path taken
print("Maze with path:")
print_maze(maze, path)

# Convert maze path to AES key
key = maze_to_key(maze, path)
print(f"Key (hex): {key.hex()}")

# Flag and encryption
flag = 'WRECKIT50{d0_y0u_th1nk_BFS_g0nna_s0lve_it?}'
iv, ct = encrypt_flag(flag, key)
print(f"Encrypted flag (iv: {iv}, ct: {ct})")

# Example usage: Decrypting (should be done after solving the maze)
decrypted_flag = decrypt_flag(iv, ct, key)
print(f"Decrypted flag: {decrypted_flag}")
