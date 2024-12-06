import re
def read_file():
    puzzle_input = open("input.txt", "r").read()
    muls = re.findall(r'mul\(\d+,\d+\)', puzzle_input)
    number_pairs = []
    for mul in muls:
        number_pairs.append(re.findall(r'\d+', mul))

    for number_pair in number_pairs:
        number_pair[0] = int(number_pair[0])
        number_pair[1] = int(number_pair[1])

    return number_pairs

def start():
    number_pairs = read_file()
    print(number_pairs)
    result = 0
    for number_pair in number_pairs:
        result += number_pair[0] * number_pair[1]

    print(result)

start()