puzzleInput = open("input.txt", "r")
puzzleRows = puzzleInput.read().split("\n")
answer = 0

## Split each row into an array of "numbers" (currently still strings)
for i, row in enumerate(puzzleRows):
    puzzleRows[i] = row.split()

for row in puzzleRows:
    startJump = (int(row[1]) - int(row[0]))
    maxJump = 3
    isSafe, isAscending = True, True
    if 0 > startJump: isAscending = False

    for i in range(1, len(row)):
        prev, curr = int(row[i-1]), int(row[i])
        currJump = (curr - prev)
        currIsAscending = True
        if 0 > currJump: currIsAscending = False

        if currJump == 0 or isAscending != currIsAscending:
            isSafe = False
            break

        if abs(curr - prev) > maxJump:
            isSafe = False
            break

    if isSafe:
        answer += 1

print(answer)