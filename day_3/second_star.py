def find_max_joltage(n: int) -> int:
    res = 0
    digits = [int(char) for char in str(n)]
    left = 0
    right = len(digits) - 12
    while right < len(digits):
        max_tuple = left, digits[left]
        for i in range(left + 1, right + 1):
            if digits[i] > digits[max_tuple[0]]:
                max_tuple = i, digits[i]
        res = res * 10 + max_tuple[1]
        right += 1
        left = max_tuple[0] + 1
    return res


lines = open("./puzzle.txt").read().splitlines()
sumjolts = 0
for line in lines:
    maxjolt = find_max_joltage(line)
    print(maxjolt)
    sumjolts += maxjolt
print (sumjolts)