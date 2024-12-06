def read_file():
    return_rows = []
    puzzle_input = open("input.txt", "r").read().split("\n")
    for row in puzzle_input:
        row_as_int = []
        row = row.split()
        for num in row: row_as_int.append(int(num))
        return_rows.append(row_as_int)

    return return_rows

def Start():
    inputRows = read_file()
    count = 0

    for row in inputRows:
        this_row_is_valid = advanced_row_is_valid(row)
        count += this_row_is_valid

    print(count)
    return count

def advanced_row_is_valid(row):
    # If row is valid without removing any number, return True
    if row_is_valid(row): return True

    # Else try popping index i for every index and check if the row is valid without it
    # (Very inefficient :D)
    for i in range(0, len(row)):
        subRow = row.copy()
        subRow.pop(i)
        if row_is_valid(subRow): return True

    return False

def row_is_valid(row):
    is_asc = row[1] > row[0]
    for i in range(1, len(row)):
        curr_num = row[i]
        prev_num = row[i - 1]
        curr_is_asc = curr_num > prev_num

        if curr_num == prev_num:
            return False

        if is_asc != curr_is_asc:
            return False

        if abs(curr_num - prev_num) > 3:
            return False

    return True

Start()