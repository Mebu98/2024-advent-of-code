def read_puzzle():
    puzzle = open("puzzle.txt", "r").read().split("\n")
    return puzzle

def solution():
    answer = 0
    rows = read_puzzle()
    diagonal1 = ((-1, 1), (1, -1))
    diagonal2 = ((1, 1), (-1,-1))

    def diagonal_is_mas(x, y, diagonal):
        top = rows[y + diagonal[0][1]][x + diagonal[0][0]]
        bottom = rows[y + diagonal[1][1]][x + diagonal[1][0]]
        if (top + bottom == "MS"
            or top + bottom == "SM"):
            return True

    for y in range (1, len(rows) - 1):
        row = rows[y]
        for x in range(1, len(row) - 1):
            char = row[x]
            if char == "A":
                if (diagonal_is_mas(x, y, diagonal1)
                    and diagonal_is_mas(x, y, diagonal2)):
                    answer += 1


    return answer

def d04s02():
    return solution()