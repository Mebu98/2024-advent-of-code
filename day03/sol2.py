import re
def read_file():
    puzzle_input = open("input.txt", "r").read()
    muls = re.findall(r'(don\'t|do)|(mul\(\d+,\d+\))', puzzle_input)
    return muls

def multiply(mul):
    num_pair = re.findall(r'\d+', mul)
    return int(num_pair[0]) * int(num_pair[1])

def start():
    p_input = read_file()
    counter = 0
    prev_order = "do"

    for mul in p_input:
        if mul[0] != "":
            prev_order = mul[0]

        if mul[1] != "" and prev_order == "do":
            counter += multiply(mul[1])

    return counter

print(start())