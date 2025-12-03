file_path: str = "./puzzle.txt"

def import_puzzle(file_path: str) -> list[list[str, str]]:
    result = []
    with open(file_path, "r") as file:
        puzzle = file.read().strip().split(",")
        for x in puzzle:
            result.append(x.split("-"))
            result[-1] = [int(i) for i in result[-1]]
        return result

def main():
    puzzle = import_puzzle(file_path)
    print(puzzle)
    result = 0
    for _range in puzzle:
        for i in range(int(_range[0]), int(_range[1]) + 1):
            number = str(i)
            middle = len(number)//2
            if number[0:middle] == number[middle:]:
                result += i
    print(result)
if __name__ == "__main__":
    main()