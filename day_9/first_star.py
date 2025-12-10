def import_puzzle(file_path: str) -> list[tuple[int, int]]:
    puzzle = []
    with open(file_path, "r") as file:
        for line in file:
            x, y = map(int, line.strip().split(","))
            puzzle.append((x, y))
    return puzzle

def find_bigger_area(puzzle: list[tuple[int, int]]) -> int:
    bigger_area = 0
    for x in puzzle:
        for y in puzzle:
            area = (abs(x[0] - y[0]) + 1)* (abs(x[1] - y[1]) + 1)
            if area > bigger_area:
                print(f"({x[0]}, {x[1]}) and ({y[0]}, {y[1]}) have an area of {abs(x[0] - y[0])+1} * {abs(x[1] - y[1])+1} = {area}")  # Uncomment this line to print coordinates
                bigger_area = area
    return bigger_area



def main():
    puzzle = import_puzzle("puzzle.txt")
    print(puzzle)
    result = find_bigger_area(puzzle)
    print(result)

if __name__ == "__main__":
    main()