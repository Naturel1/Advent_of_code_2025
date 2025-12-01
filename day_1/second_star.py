file_path: str = "./puzzle.txt"


def import_puzzle() -> list[str]:
    with open(file_path, "r") as file:
        puzzle = [line.strip() for line in file]
        return puzzle


def main():
    dial: int = 50
    result: int = 0
    puzzle: list[str] = import_puzzle()
    print(f"Puzzle: {puzzle}")
    for move in puzzle:
        current_dial: int = dial
        if move.startswith("R"):
            for _ in range(int(move[1:])):
                if dial == 99:
                    dial = 0
                else:
                    dial += 1
                if dial == 0:
                    result += 1
                    print("pass 0")
        elif move.startswith("L"):
            for _ in range(int(move[1:])):
                if dial == 0:
                    dial = 99
                else:
                    dial -= 1
                if dial == 0:
                    result += 1
                    print("pass 0")
        print(f"Moved {move} and dial now at {dial}")
    print(f"Final dial position: {dial}")
    print(f"Number of positions marked: {result}")

if __name__ == "__main__":
    main()