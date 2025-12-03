from tqdm import tqdm


def import_puzzle(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        puzzle = [line.strip() for line in file]
        return puzzle

def check_battery(batteries: str) -> int:
    bigger_batterie = 0
    print(f"Battery: {batteries}")
    for i in range(len(batteries)):
        for j in range(i+1, len(batteries)):
            if int(batteries[i] + batteries[j]) > bigger_batterie:
                bigger_batterie = int(batteries[i] + batteries[j])
                print(f"Bigger battery: {int(batteries[i] + batteries[j])}")
    return bigger_batterie


def main():
    file_path = "./puzzle.txt"
    result = 0
    puzzle = import_puzzle(file_path)
    print(f"Puzzle: {puzzle}")
    for line in tqdm(puzzle):
        result += check_battery(line)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()