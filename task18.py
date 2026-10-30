maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
]

def solve_maze(x, y, path, visited):
    n = len(maze)

    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if maze[x][y] == 1 or (x, y) in visited:
        return False

    path.append((x, y))
    visited.add((x, y))

    if x == n - 1 and y == n - 1:
        return True


    if (solve_maze(x + 1, y, path, visited) or
            solve_maze(x, y + 1, path, visited) or
            solve_maze(x - 1, y, path, visited) or
            solve_maze(x, y - 1, path, visited)):
        return True

    path.pop()
    return False

path = []
if solve_maze(0, 0, path, set()):
    print("Путь:", path)
else:
    print("Пути нет")