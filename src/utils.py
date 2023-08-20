import json
from pathlib import Path


local_path = Path()
DB_PATH = local_path.absolute().parent.joinpath("data/books.json")


def bool_input(prompt: str) -> bool:
    """
    :param prompt: String to ask user.
    :return: Returns True if user inputs 'yes' and False if user inputs 'no'
    """
    while True:
        i = input(prompt)
        match i.lower():
            case "y" | "yes":
                return True
            case "n" | "no":
                return False
            case _:
                print("Input must be 'y' or 'n'.\n")


def rev_bool_input(prompt: str) -> bool:
    """
    :param prompt: String to ask user
    :return: Returns False if user inputs 'yes' and True if user inputs 'no'
    """
    return True if bool_input(prompt) is False else False


def list_input(prompt: str, separator: str) -> list[str]:
    """
    :param prompt: The text you want the program to display.
    :param separator: The separator character used to separate items in the list.
    :return:
    """
    i = input(prompt)
    items = i.split(separator)
    return items


def int_input(prompt: str, floor_val: int, ceil_val: int = 10_000) -> int:
    while True:
        i = input(prompt)
        try:
            i = int(i)
            if floor_val <= i <= ceil_val:
                return i
            else:
                print(f"Integer must be between {floor_val} and {ceil_val}")
        except ValueError:
            print(f"'{i}' is not a valid integer.")


def get_db() -> list[dict]:
    """
    :return: dictionary of json elements in books.json
    """
    with open(DB_PATH, "r") as f:
        data = json.load(f)
    return data


def update_db(entry: list[dict]):
    with open(DB_PATH, "w") as f:
        json.dump(entry, f, indent=4)
