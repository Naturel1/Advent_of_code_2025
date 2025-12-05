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

def is_ingredient_fresh(ingredient: int, menu: dict) -> bool:
    for start, end in zip(menu["start"], menu["end"]):
        if start <= ingredient <= end:
            return True
    return False

def main():
    result = 0
    menu_range, ingredients_list = import_puzzle("puzzle.txt")
    print(menu_range, ingredients_list)
    for ingredient in tqdm(ingredients_list):
        if is_ingredient_fresh(ingredient, menu_range):
            result += 1
    print(result)

if __name__ == "__main__":
    main()