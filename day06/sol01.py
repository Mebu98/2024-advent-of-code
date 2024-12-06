def read_puzzle():
    puzzle = open("puzzle.txt", "r").read()
    grid = puzzle.split("\n")
    return grid

def find_guard(grid):
    guard = ['^', '>', 'v','<']
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char in guard:
                return [x, y, char]
    return None

def find_obstacles(grid):
    obstacle = "#"
    obstacles = []
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char == obstacle: obstacles.append([x, y])
    return obstacles

def find_path(guard, obstacles, max_x, max_y):
    ## Guard has [X, Y, Direction(which can be ^, >, v, <)]
    ## Obstacles have all obstacle X and Y positions
    count = 0
    directions = ['^', '>', 'v', '<']
    direction = directions.index(guard[2])

    return count

def d06s01start():
    grid = read_puzzle()
    guard = find_guard(grid)
    obstacles = find_obstacles(grid)
    count = find_path(guard, obstacles, len(grid), len(grid[0]))
    print(count)
    return "Hello World"