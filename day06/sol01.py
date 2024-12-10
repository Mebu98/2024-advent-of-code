class Guard:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Step:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

def read_puzzle():
    puzzle = open("puzzle.txt", "r").read()
    grid = puzzle.split("\n")
    for i in range(0, len(grid)):
        grid[i] = list(grid[i])
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
            if char == obstacleChar:
                obstacle = Obstacle(x, y)
                obstacles.append(obstacle)
    return obstacles

def calc_steps(guard, obstacles, max_x, max_y):
    ## Guard has [X, Y, Direction(which can be ^, >, v, <)]
    ## Obstacles are all obstacle X and Y positions
    steps = [Step(guard.x, guard.y, "S")]

    while (0 < guard.x < max_x
           and 0 < guard.y < max_y):
        closest_obstacle = find_closest_obstacle(guard, obstacles)
        current_steps = []

        ## if closest obstacle is none then it means we have hit all obstacles and are on our way out of the map
        if closest_obstacle is None:
            print(f'Guard is moving out of bounds from: {guard.x}, {guard.y}')
            if guard.direction == "^":
                print("Guard moving up out of bounds")
                for i in range(guard.y, -1, -1):
                    current_steps.append(Step(guard.x, i, guard.direction))
                    guard.y = max_y + 1

            elif guard.direction == ">":
                print("Guard moving right out of bounds")
                for i in range(guard.x, max_x):
                    current_steps.append(Step(i, guard.y, guard.direction))
                    guard.x = max_x + 1

            elif guard.direction == "v":
                print("Guard moving down out of bounds")
                for i in range(guard.y, max_y):
                    current_steps.append(Step(guard.x, i, guard.direction))
                    guard.y = -1

            elif guard.direction == "<":
                print("Guard moving left out of bounds")
                for i in range(guard.x, -1, -1):
                    current_steps.append(Step(i, guard.y, guard.direction))
                    guard.x = -1

        ## Else we're walking to an obstacle on the X axis
        elif closest_obstacle.x is guard.x:
            if closest_obstacle.y < guard.y:
                print("Guard moving up")
                for i in range(guard.y, closest_obstacle.y + 1, -1):
                    current_steps.append(Step(guard.x, i, guard.direction))
                guard = Guard(closest_obstacle.x, closest_obstacle.y + 1, ">")
            else:
                print("Guard moving down")
                for i in range(guard.y, closest_obstacle.y - 1):
                    current_steps.append(Step(guard.x, i, guard.direction))
                guard = Guard(closest_obstacle.x, closest_obstacle.y - 1, "<")

        ## Or on the Y axis
        else:
            if closest_obstacle.x < guard.x:
                print("Guard moving left")
                for i in range(guard.x, closest_obstacle.x + 1, -1):
                    current_steps.append(Step(i, guard.y, guard.direction))
                guard = Guard(closest_obstacle.x + 1, closest_obstacle.y, "^")
            else:
                print("Guard moving right")
                for i in range(guard.x, closest_obstacle.x - 1):
                    current_steps.append(Step(i, guard.y, guard.direction))
                guard = Guard(closest_obstacle.x - 1, closest_obstacle.y, "v")


        for step in current_steps:
            steps.append(step)
    return steps

def find_closest_obstacle(guard, obstacles):
    closest_obstacle = None

    for obstacle in obstacles:
        ## If obstacle is in line with the guard in either X or Y direction
        if obstacle.x == guard.x or obstacle.y == guard.y:
            ## GuardY > obsY because Y goes from top to bottom
            if guard.direction == "^" and guard.y > obstacle.y:
                if closest_obstacle is None or guard.y - obstacle.y < guard.y - closest_obstacle.y:
                    closest_obstacle = obstacle

            if guard.direction == ">" and guard.x < obstacle.x:
                if closest_obstacle is None or obstacle.x - guard.x < closest_obstacle.x - guard.x:
                    closest_obstacle = obstacle

            if guard.direction == "v" and guard.y < obstacle.y:
                if closest_obstacle is None or obstacle.y - guard.y < closest_obstacle.y - guard.y:
                    closest_obstacle = obstacle

            if guard.direction == "<" and guard.x > obstacle.x:
                if closest_obstacle is None or guard.x - obstacle.x < guard.x - closest_obstacle.x:
                    closest_obstacle = obstacle

    return closest_obstacle

def d06s01start():
    grid = read_puzzle()
    guard = find_guard(grid)
    obstacles = find_obstacles(grid)
    steps = calc_steps(guard, obstacles, len(grid), len(grid[0]))
    unique_steps = [steps[0]]
    for step in steps:
        is_in = False
        for unique_step in unique_steps:
            if step.x == unique_step.x and step.y == unique_step.y: is_in = True

        if is_in is False: unique_steps.append(step)

    print(f'Unique coordinates touched: {len(unique_steps)}')

    grid_string = ""

    for y in range (0, len(grid)):
        for x in range(0, len(grid[0])):
            for step in unique_steps:
                if step.x == x and step.y == y:
                    grid[y][x] = step.direction

            for obstacle in obstacles:
                if obstacle.x == x and obstacle.y == y:
                    grid[y][x] = "#"

    for row in grid:
        for letter in row:
            grid_string += letter
        grid_string += "\n"
    print(grid_string)

    return len(unique_steps)