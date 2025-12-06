from math import prod

data = open("puzzle.txt").read().splitlines()
operands = data[-1].split()
tot = 0
op = 0
nums = []
for j in range(0, len(data[0])):
    pos_num = ""
    # Get the column number.
    for i in range(0, len(data) - 1):
        if data[i][j] != " ":
            pos_num += data[i][j]

    # If the column number is all whitespace,
    # then the numbers end, and you operate them.
    # Same if it is the last column.
    if pos_num == "" or j == len(data[0]) - 1:
        if j == len(data[0]) - 1:
            nums.append(int(pos_num))
        operand = operands[op]
        if operand == '*':
            tot += prod(nums)
        else:
            tot += sum(nums)
        nums = []
        op += 1

    # If the column contains some number,
    # delete the whitespace and add the number.
    else:
        nums.append(int(pos_num))
print(tot)