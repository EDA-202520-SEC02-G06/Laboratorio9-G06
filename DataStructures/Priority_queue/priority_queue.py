from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import pq_entry as pqe


def default_compare_higher_value(father_node, child_node):
    if child_node is None:
        return True
    if father_node is None:
        return False
    return pqe.get_priority(father_node) >= pqe.get_priority(child_node)


def default_compare_lower_value(father_node, child_node):
    if child_node is None:
        return True
    if father_node is None:
        return False
    return pqe.get_priority(father_node) <= pqe.get_priority(child_node)


def new_heap(is_min_pq=True):
    cmp_fun = default_compare_lower_value if is_min_pq else default_compare_higher_value

    elements = lt.new_list()
    lt.add_last(elements, None)

    return {
        "elements": elements,
        "size": 0,
        "cmp_function": cmp_fun,
        "is_min_pq": is_min_pq,
    }


def insert(my_heap, priority, value):
    entry = pqe.new_pq_entry(priority, value)

    lt.add_last(my_heap["elements"], entry)
    my_heap["size"] += 1
    _swim(my_heap, my_heap["size"])


def is_empty(my_heap):
    return my_heap["size"] == 0


def size(my_heap):
    return my_heap["size"]


def get_first_priority(my_heap):
    if is_empty(my_heap):
        return None
    return pqe.get_priority(_get_entry(my_heap, 1))


def remove(my_heap):
    if is_empty(my_heap):
        return None

    root_entry = _get_entry(my_heap, 1)

    if my_heap["size"] == 1:
        lt.remove_last(my_heap["elements"])
        my_heap["size"] = 0
    else:
        lt.exchange(my_heap["elements"], 1, my_heap["size"])
        lt.remove_last(my_heap["elements"])
        my_heap["size"] -= 1
        _sink(my_heap, 1)

    return pqe.get_value(root_entry)


def contains(my_heap, value):
    return is_present_value(my_heap, value) != -1


def is_present_value(my_heap, value):
    for index in range(1, my_heap["size"] + 1):
        entry = _get_entry(my_heap, index)
        if entry is not None and pqe.get_value(entry) == value:
            return index
    return -1


def _get_entry(my_heap, position):
    return lt.get_element(my_heap["elements"], position)


def _swim(my_heap, position):
    while position > 1:
        parent = position // 2
        if my_heap["cmp_function"](_get_entry(my_heap, parent), _get_entry(my_heap, position)):
            break
        lt.exchange(my_heap["elements"], parent, position)
        position = parent


def _sink(my_heap, position):
    while 2 * position <= my_heap["size"]:
        child = 2 * position

        if child < my_heap["size"]:
            left = _get_entry(my_heap, child)
            right = _get_entry(my_heap, child + 1)
            if not my_heap["cmp_function"](left, right):
                child += 1

        if my_heap["cmp_function"](_get_entry(my_heap, position), _get_entry(my_heap, child)):
            break

        lt.exchange(my_heap["elements"], position, child)
        position = child
