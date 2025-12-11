
def import_puzzle(file_path: str) -> dict[list[str]]:
    puzzle = {}
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(": ")
            key = parts[0]
            value = parts[1].split(" ")
            puzzle[key] = value
    return puzzle

def path_finding(puzzle: dict[list[str]], start: str, end: str) -> list[list[str]]:
    """Find every possible path from start to end, considering the given puzzle."""
    all_paths = []
    
    def dfs(current: str, target: str, visited: set[str], path: list[str]):
        """Depth-first search to find all paths."""
        if current == target:
            all_paths.append(path.copy())
            return
        
        if current not in puzzle:
            return
        
        for neighbor in puzzle[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                dfs(neighbor, target, visited, path)
                path.pop()
                visited.remove(neighbor)
    
    visited = {start}
    dfs(start, end, visited, [start])
    
    return all_paths

def main():
    file_path = "./puzzle.txt"
    puzzle = import_puzzle(file_path)
    print(puzzle)
    paths = path_finding(puzzle, "you", "out")
    print(paths)
    print(len(paths))


if __name__ == "__main__":
    main()
