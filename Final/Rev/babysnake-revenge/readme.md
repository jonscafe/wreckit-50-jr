## author: k.eii

### babysnake on the quals is taking a revenge!
### POC:
- BFS to solve the Maze and get the key (based on the path to solve the maze)

```def genKey(path):
    key = bytearray(16)
    for i, (x, y) in enumerate(path):
        key[i % len(key)] ^= (x + y) % 256
    return bytes(key)```
