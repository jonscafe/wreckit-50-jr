import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from collections import deque
import random

def create_maze(width, height):
    # Initialize maze with walls
    maze = [['#' for _ in range(width)] for _ in range(height)]

    # Create a path using a simple maze generation algorithm
    def create_path(x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # Right, Down, Left, Up
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == '#':
                if dx == 0:
                    maze[y + dy // 2][x] = '.'
                else:
                    maze[y][x + dx // 2] = '.'
                maze[ny][nx] = '.'
                create_path(nx, ny)

    # Start creating the path from the top-left corner
    maze[1][1] = '.'
    create_path(1, 1)

    # Ensure start and end are open
    maze[1][1] = '.'
    maze[height - 2][width - 2] = '.'

    return [''.join(row) for row in maze]

# Create a 50x50 maze
maze = create_maze(50, 50)

# Define start and end positions for the maze
start = (1, 1)
end = (48, 48)

def generate_key(path):
    key = bytearray(16)
    for i, (x, y) in enumerate(path):
        key[i % len(key)] ^= (x + y) % 256
    return bytes(key)

def decrypt_flag(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode('utf-8')

iv = base64.b64decode("mJKl/x5xJ1viL34VEVDI7g==")
ciphertext = base64.b64decode("KfjOvI6aG2qnnLYjC2h4bsw86qYrDglEXu4+Ia7rekhPwwnZIkUEvDP7Qn6msdt/")

def bfs_solve_maze(maze, start, end):
    queue = deque([([start], start)])
    visited = set()
    visited.add(start)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    while queue:
        path, current = queue.popleft()
        if current == end:
            return path

        for direction in directions:
            next_position = (current[0] + direction[0], current[1] + direction[1])
            if (
                0 <= next_position[0] < len(maze)
                and 0 <= next_position[1] < len(maze[0])
                and maze[next_position[0]][next_position[1]] == '.'
                and next_position not in visited
            ):
                visited.add(next_position)
                queue.append((path + [next_position], next_position))

    return None

def solve_maze():
    print("Solving the maze using BFS...")

    # Find the path using BFS
    path = bfs_solve_maze(maze, start, end)

    if path:
        user_key = generate_key(path)
        hex_key = user_key.hex()

        # Print maze with quotation marks and comma
        print(f'"{maze[0]}",')  # Print the first line of the maze with quotation marks and comma
        for line in maze[1:]:
            print(f'"{line}",')
        print(f"Hex key: {hex_key}")
        
        # Decrypt the flag
        flag = decrypt_flag(user_key, iv, ciphertext)
        print(f"Correct path found! Decrypted flag: {flag}")
    else:
        print("No path found!")

# Run the solution
solve_maze()
