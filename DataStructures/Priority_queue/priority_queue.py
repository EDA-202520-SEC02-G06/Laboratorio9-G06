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

