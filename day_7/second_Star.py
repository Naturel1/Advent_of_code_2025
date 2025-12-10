from copy import deepcopy
from time import sleep


def import_puzzle(path: str) -> list[list[str]]:
    puzzle = []
    with open(path, "r") as file:
        for line in file:
            puzzle.append(list(line.strip()))
    return puzzle

def visualize_puzzle(puzzle: list[list[str]], pos):
    _puzzle = deepcopy(puzzle)
    _puzzle[pos[0]][pos[1]] = "X"

    for row in _puzzle:
        print("".join(row))
    print()
    sleep(0.1)

def main():
    puzzle = import_puzzle("puzzle.txt")
    result = 0
    start = [0, puzzle[0].index("S")]
    parcours = [start]
    while len(parcours)>0:
        current = parcours.pop()
        while current[0] < len(puzzle)-1:
            current[0] += 1
            if puzzle[current[0]][current[1]] == "^":
                parcours.append([current[0], current[1]+1])
                current[1] -= 1
            # visualize_puzzle(puzzle, current)
        result += 1
    print(result)

if __name__ == "__main__":
    main()
