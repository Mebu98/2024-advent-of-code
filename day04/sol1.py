def read_puzzle():
    puzzle = open("puzzle.txt", "r").read().split("\n")
    return puzzle

def solution():
    rows = read_puzzle()
    count = 0
    max_x = len(rows[0])
    max_y = len(rows)

    def has_xmas(x, y, direction):

        for i, char in enumerate("XMAS"):
            curr_x = x + (i * direction[0])
            curr_y = y + (i * direction[1])
            ## Make sure we don't try to access an out-of-bounds index
            if not (0 <= curr_x < max_x and 0 <= curr_y < max_y):
                return False
            if rows[curr_y][curr_x] != char:
                return False

        return True

    for y in range(max_y):
        for x in range(max_x):
            for dir_x in range(-1, 2):
                for dir_y in range(-1, 2):
                    count += has_xmas(x, y, (dir_x, dir_y))

    return count

def d04s01():
    return solution()