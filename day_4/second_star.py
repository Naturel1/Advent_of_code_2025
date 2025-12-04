def import_puzzle(file_path: str) -> list[str]:
    puzzle = []
    with open(file_path, "r") as file:
        for line in file:
            puzzle.append(list(line.strip()))
    return puzzle


def count_adjacent_at_signs(puzzle: list[list[str]], y: int, x: int) -> int:
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dy, dx in directions:
        new_y, new_x = y + dy, x + dx
        if 0 <= new_y < len(puzzle) and 0 <= new_x < len(puzzle[new_y]):
            if puzzle[new_y][new_x] == "@":
                count += 1
    return count

def visualize_puzzle(puzzle: list[list[str]]) -> str:
    result = ""
    for row in puzzle:
        result += "".join(row) + "\n"
    return result


def main():
    result = 0
    removable = []
    puzzle = import_puzzle("puzzle.txt")
    print(puzzle)
    while True:
        for y in range(len(puzzle)):
            for x in range(len(puzzle[y])):
                if puzzle[y][x] == "@":
                    adjacent_count = count_adjacent_at_signs(puzzle, y, x)
                    if adjacent_count < 4:
                        result += 1
                        removable.append((y, x))
                    # print(f"Position ({y}, {x}): {adjacent_count} adjacent '@' symbols")
        for x in removable:
            puzzle[x[0]][x[1]] = "."
        print(visualize_puzzle(puzzle))
        if len(removable) == 0:
            break
        else:
            removable = []

    print(result)


if __name__ == "__main__":
    main()
