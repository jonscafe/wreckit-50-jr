## author: k.eii

### babysnake on the quals is taking a revenge!
### POC:
- BFS to solve the Maze and get the key (based on the path to solve the maze)

```def genKey(path):
    key = bytearray(16)
    for i, (x, y) in enumerate(path):
        key[i % len(key)] ^= (x + y) % 256
    return bytes(key)```

Solving the maze using BFS...
Hex key: 1615742b2a2930111211780908680016
Correct path found! Decrypted flag: WRECKIT50{d0_y0u_th1nk_BFS_g0nna_s0lve_it?}
