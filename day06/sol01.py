class Guard:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def read_puzzle():
    puzzle = open("puzzle.txt", "r").read()
    grid = puzzle.split("\n")
    return grid

def find_guard(grid):
    guardDirection = ['^', '>', 'v','<']
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char in guardDirection:
                guard = Guard(x, y, char)
                return guard
    return None

def find_obstacles(grid):
    obstacleChar = "#"
    obstacles = []
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            obs = Obstacle(x, y)
            if char == obstacleChar: obstacles.append(obs)
    return obstacles

def calc_steps(guard, obstacles, max_x, max_y):
    ## Guard has [X, Y, Direction(which can be ^, >, v, <)]
    ## Obstacles are all obstacle X and Y positions
    steps = []

    while (0 < guard.x < max_x
           and 0 < guard.y < max_y):
        closest_obstacle = find_closest_obstacle(guard, obstacles)
        current_steps = []

        ## if closest obstacle is none then it means we have hit all obstacles and are on our way out of the map
        if closest_obstacle.x is None:
            print(f'Guard is moving out of bounds from: {guard.x}, {guard.y}')
            if guard.direction == "^":
                print("Guard moving up out of bounds")
                for i in range(0, guard.y):
                    current_steps.append([guard.x, i])
                    guard.y = max_y + 1

            elif guard.direction == ">":
                print("Guard moving right out of bounds")
                for i in range(guard.x, max_x):
                    current_steps.append([i, guard.y])
                    guard.x = max_x + 1

            elif guard.direction == "v":
                print("Guard moving down out of bounds")
                for i in range(guard.y, max_y):
                    current_steps.append([guard.x, i])
                    guard.y = -1

            elif guard.direction == "<":
                print("Guard moving left out of bounds")
                for i in range(0, guard.x):
                    current_steps.append([i, guard.y])
                    guard.x = -1

        elif closest_obstacle.x is guard.x:
            if closest_obstacle.y < guard.y:
                print("Guard moving up")
                for i in range(closest_obstacle.y + 1, guard.y):
                    current_steps.append([guard.x, i])
                guard = Guard(closest_obstacle.x, closest_obstacle.y + 1, ">")
            else:
                print("Guard moving down")
                for i in range(guard.y, closest_obstacle.y -1):
                    current_steps.append([guard.x, i])
                guard = Guard(closest_obstacle.x, closest_obstacle.y - 1, "<")

        else:
            if closest_obstacle.x < guard.x:
                print("Guard moving left")
                for i in range(closest_obstacle.x + 1, guard.x):
                    current_steps.append([i, guard.y])
                guard = Guard(closest_obstacle.x + 1, closest_obstacle.y, "^")
            else:
                print("Guard moving right")
                for i in range(guard.x, closest_obstacle.x -1):
                    current_steps.append([i, guard.y])
                guard = Guard(closest_obstacle.x - 1, closest_obstacle.y, "v")

        for step in current_steps:
            steps.append(step)

    print(f'steps: {steps}')
    return steps


def find_closest_obstacle(guard, obstacles):
    closest_obstacle = Obstacle(None, None)

    for obstacle in obstacles:
        if obstacle.x == guard.x or obstacle.y == guard.y:
            ## GuardY > obsY because Y goes from top to bottom
            if guard.direction == "^" and guard.y > obstacle.y:
                if closest_obstacle.x is None or guard.y - obstacle.y < guard.y - closest_obstacle.y:
                    closest_obstacle = obstacle

            if guard.direction == ">" and guard.x < obstacle.x:
                if closest_obstacle.x is None or guard.y - obstacle.y < guard.y - closest_obstacle.y:
                    closest_obstacle = obstacle

            if guard.direction == "v" and guard.y < obstacle.y:
                if closest_obstacle.x is None or guard.y - obstacle.y < guard.y - closest_obstacle.y:
                    closest_obstacle = obstacle

            if guard.direction == "<" and guard.x > obstacle.x:
                if closest_obstacle.x is None or guard.y - obstacle.y < guard.y - closest_obstacle.y:
                    closest_obstacle = obstacle

    return closest_obstacle

def d06s01start():
    grid = read_puzzle()
    guard = find_guard(grid)
    obstacles = find_obstacles(grid)
    steps = calc_steps(guard, obstacles, len(grid), len(grid[0]))
    unique_steps = []
    for step in steps:
        if step not in unique_steps: unique_steps.append(step)

    return len(unique_steps)