def import_puzzle(path: str) -> list[list[str]]:
    puzzle = []
    with open(path, "r") as file:
        for line in file:
            puzzle.append(list(line.strip()))
    return puzzle

def visualize_puzzle(puzzle: list[list[str]]):
    for row in puzzle:
        print("".join(row))
    print()

def main():
    result = 0
    puzzle = import_puzzle("puzzle.txt")
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            if puzzle[y][x] == "S":
                if y < len(puzzle)-1 and puzzle[y + 1][x] == ".":
                    puzzle[y + 1][x] = "|"
            if puzzle[y][x] == "|":
                if y < len(puzzle)-1 and puzzle[y + 1][x] == ".":
                    puzzle[y + 1][x] = "|"
                elif y < len(puzzle)-1 and puzzle[y + 1][x] == "^":
                    puzzle[y + 1][x - 1] = "|"
                    puzzle[y + 1][x + 1] = "|"
        visualize_puzzle(puzzle)
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            if puzzle[y][x] == "^" and puzzle[y - 1][x] == "|":
                result += 1
    print(result)


if __name__ == "__main__":
    main()