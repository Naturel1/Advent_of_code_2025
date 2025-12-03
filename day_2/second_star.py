import re

from tqdm import tqdm

file_path: str = "./puzzle.txt"

def import_puzzle(file_path: str) -> list[list[str, str]]:
    result = []
    with open(file_path, "r") as file:
        puzzle = file.read().strip().split(",")
        for x in puzzle:
            result.append(x.split("-"))
            result[-1] = [int(i) for i in result[-1]]
        return result

def is_valid_number(number: str) -> bool:
    result = False
    for i in range(1, len(number) // 2 + 1):
        if len(number) % i == 0:
            if number[:i] * (len(number) // i) == number:
                result = True
                break
    return result

def main():
    puzzle = import_puzzle(file_path)
    print(puzzle)
    result = 0
    for _range in tqdm(puzzle):
        for i in range(int(_range[0]), int(_range[1]) + 1):
            number = str(i)
            if is_valid_number(number):
                result += i
    print(result)
if __name__ == "__main__":
    main()