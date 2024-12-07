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
    steps = [[guard.x, guard.y]]

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
                for i in range(guard.x, -1, -1):
                    current_steps.append([i, guard.y])
                    guard.x = -1

        ## Else we're walking to an obstacle on the X axis
        elif closest_obstacle.x is guard.x:
            if closest_obstacle.y < guard.y:
                print("Guard moving up")
                for i in range(guard.y, closest_obstacle.y + 1, -1):
                    current_steps.append([guard.x, i])
                guard = Guard(closest_obstacle.x, closest_obstacle.y + 1, ">")
            else:
                print("Guard moving down")
                for i in range(guard.y, closest_obstacle.y - 1):
                    current_steps.append([guard.x, i])
                guard = Guard(closest_obstacle.x, closest_obstacle.y - 1, "<")

        ## Or on the Y axis
        else:
            if closest_obstacle.x < guard.x:
                print("Guard moving left")
                for i in range(guard.x, closest_obstacle.x + 1, -1):
                    current_steps.append([i, guard.y])
                guard = Guard(closest_obstacle.x + 1, closest_obstacle.y, "^")
            else:
                print("Guard moving right")
                for i in range(guard.x, closest_obstacle.x - 1):
                    current_steps.append([i, guard.y])
                guard = Guard(closest_obstacle.x - 1, closest_obstacle.y, "v")

        print(f'{len(current_steps)} steps: {current_steps}')

        for step in current_steps:
            steps.append(step)

    print(f'steps: {steps}')
    print (len(steps))
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
    unique_steps = []
    # for step in steps:
    #     if step not in unique_steps:
    #         unique_steps.append(step)
    #     else:
    #         print(f'{step} is already in unique steps')

    # for y in range (0, len(grid)):
    #     for x in range(0, len(grid[0])):
    #         for step in unique_steps:
    #             if step[0] == x and step[1] == y:
    #                 print(step)
    #                 grid[y][x] = "X"
    #
    #         for obstacle in obstacles:
    #             if obstacle.x == x and obstacle.y == y:
    #                 grid[y][x] = "#"
    #
    # for row in grid:
    #     print(row)
    return len(unique_steps)