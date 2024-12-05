def ReadFile():
    returnRows = []
    puzzleInput = open("input.txt", "r").read().split("\n")
    for row in puzzleInput:
        rowAsInt = []
        row = row.split()
        for num in row: rowAsInt.append(int(num))
        returnRows.append(rowAsInt)

    return returnRows

def Start():
    inputRows = ReadFile()
    count = 0

    for row in inputRows:
        rowIsValid = AdvancedRowIsValid(row)
        count += rowIsValid

    print(count)
    return count

def AdvancedRowIsValid(row):
    # If row is valid without removing any number, return True
    if RowIsValid(row): return True

    # Else try popping index i for every index and check if the row is valid without it
    # (Very inefficient :D)
    for i in range(0, len(row)):
        subRow = row.copy()
        subRow.pop(i)
        if RowIsValid(subRow): return True

    return False

def RowIsValid(row):
    isAsc = row[1] > row[0]
    for i in range(1, len(row)):
        currNum = row[i]
        prevNum = row[i - 1]
        currIsAsc = currNum > prevNum

        if currNum == prevNum:
            return False

        if isAsc != currIsAsc:
            return False

        if abs(currNum - prevNum) > 3:
            return False

    return True

Start()