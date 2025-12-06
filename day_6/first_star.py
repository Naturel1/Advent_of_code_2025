import math


def input_puzzle(path_to_file: str) -> tuple[list[list[int | str]], list[str]]:
    puzzle = []
    puzzle_calc = []
    with open(path_to_file, "r") as file:
        for line in file:
            _temp = line.strip().split()
            for i in range(len(_temp)):
                try:
                    puzzle[i].append(int(_temp[i]))
                except IndexError:
                    puzzle.append([int(_temp[i])])
                except ValueError:
                    puzzle_calc.append(_temp[i])
        print(puzzle)
        print(puzzle_calc)

    return puzzle, puzzle_calc

def calculate_puzzle(puzzle: list[list[int | str]], puzzle_calc: list[str]) -> int:
    result = 0
    for col in range(len(puzzle)):
        if puzzle_calc[col] == "+":
            result += sum(puzzle[col])
            print(f"Sum of column {col}: {result}")
        elif puzzle_calc[col] == "*":
            result += math.prod(puzzle[col])
            print(f"Product of column {col}: {result}")
    return result

def main():
    puzzle, puzzle_calc = input_puzzle("puzzle.txt")
    result = calculate_puzzle(puzzle, puzzle_calc)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()