"""Simple array list abstraction with 1-based helper operations."""


def new_list() -> dict:
    """Return a new array-backed list structure."""
    return {"elements": []}


def size(array_list: dict) -> int:
    """Return the number of stored elements."""
    return len(array_list["elements"])


def add_last(array_list: dict, element) -> None:
    """Append an element at the end of the structure."""
    array_list["elements"].append(element)


def get_element(array_list: dict, position: int):
    """Return the element stored at the given position (0-based friendly)."""
    return array_list["elements"][position]


def change_info(array_list: dict, position: int, element) -> None:
    """Replace the element stored at the given position."""
    array_list["elements"][position] = element


def exchange(array_list: dict, pos1: int, pos2: int) -> None:
    """Swap the values stored at the received positions."""
    elements = array_list["elements"]
    elements[pos1], elements[pos2] = elements[pos2], elements[pos1]


def remove_last(array_list: dict):
    """Remove and return the element stored at the last position."""
    return array_list["elements"].pop() if array_list["elements"] else None
