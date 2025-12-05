
from tqdm import tqdm


def import_puzzle(file_path: str) -> tuple[dict, list[int]]:
    with open(file_path, "r") as file:
        menu, ingredients = file.read().strip().split("\n\n")
        menu_range = {"start": [], "end": []}
        ingredients_list = [int(ingredient) for ingredient in ingredients.split("\n")]
        for line in tqdm(menu.split("\n")):
            start, end = map(int, line.split("-"))
            menu_range["start"].append(start)
            menu_range["end"].append(end)

    return menu_range, ingredients_list


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []
    
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    return merged


def count_numbers_in_ranges(ranges: list[tuple[int, int]]) -> int:
    merged = merge_ranges(ranges)
    total = 0
    for start, end in merged:
        total += end - start + 1
    return total


def main():
    menu_range, _ = import_puzzle("puzzle.txt")
    
    ranges = list(zip(menu_range["start"], menu_range["end"]))
    
    result = count_numbers_in_ranges(ranges)
    
    print(f"Nombre total de numéros uniques dans le menu: {result}")


if __name__ == "__main__":
    main()
