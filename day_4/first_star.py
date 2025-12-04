
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

def main():
    result = 0
    puzzle = import_puzzle("puzzle.txt")
    print(puzzle)
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == "@":
                adjacent_count = count_adjacent_at_signs(puzzle, y, x)
                if adjacent_count < 4:
                    result += 1
                print(f"Position ({y}, {x}): {adjacent_count} adjacent '@' symbols")

    print(result)
if __name__ == "__main__":
    main()
