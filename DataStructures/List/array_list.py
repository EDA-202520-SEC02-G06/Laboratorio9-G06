<<<<<<< HEAD
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
=======
def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list['elements'][index]   

def is_present(my_list, element,cmp_function):
    
    size = my_list['size']
    
    if size > 0 :
        keyexist = False
        for keypos in range(size):
            info = my_list['elements'][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    if my_list['size'] > 0:
        return my_list['elements'][0]
    return None

def is_empty(my_list):
    if my_list['size'] == 0:
        return True
    return False

def last_element(my_list):
    if my_list['size'] > 0:
        return my_list['elements'][-1]
    else:
        raise IndexError("list index out of range")

def delete_element(my_list, pos):
    if 0 <= pos < my_list['size']:
        del my_list['elements'][pos]
        my_list['size'] -= 1
        return my_list
    else:
        raise IndexError("list index out of range")

def remove_first(my_list):
    if my_list['size'] > 0:
        first = my_list['elements'].pop(0)
        my_list['size'] -= 1
        return first
    else:
        raise IndexError("list index out of range")
def remove_last(my_list):
    if my_list['size'] > 0:
        last = my_list['elements'].pop()
        my_list['size'] -= 1
        return last
    else:
        raise IndexError("list index out of range")

def insert_element(my_list, element, pos):
    my_list['elements'].insert(pos, element)
    my_list['size'] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if 0 <= pos < my_list['size']:
        my_list['elements'][pos] = new_info
        return my_list
    else:
        raise IndexError("list index out of range")

def exchange(my_list, pos1, pos2):
    if 0 <= pos1 < my_list['size'] and 0 <= pos2 < my_list['size']:
        cambio = my_list['elements'][pos1]
        my_list['elements'][pos1] = my_list['elements'][pos2]
        my_list['elements'][pos2] = cambio
        return my_list
    else:
        raise IndexError("list index out of range")
    
def sub_list(my_list,pos_i,num_elements):
    if 0 <= pos_i < my_list['size']:
        sub_elements = my_list['elements'][pos_i:pos_i + num_elements]
        new_list = {
            'elements': sub_elements,
            'size': len(sub_elements),
        }
        return new_list
    else:
        raise IndexError("list index out of range")
    
def default_sort_criteria(element1, element2):
    if element1 < element2:
        return True
    return False

def selection_sort(my_list,sort_crit):
    elements = my_list['elements']
    size = my_list['size']
    for i in range(size):
        min_index = i
        for j in range(i+1,size):
            if sort_crit(elements[min_index],elements[j]):
                min_index = j
        exchange(my_list,i,min_index)
    return my_list
    
def insertion_sort(my_list,sort_crit):
    elements = my_list['elements']
    size = my_list["size"]
    for i in range(size):
        ancla = elements[i]
        j=i-1
        while j >= 0 and sort_crit(ancla,elements[j]) == False:
            exchange(my_list,j+1,j)
            j -= 1
        elements[j+1] = ancla
    return my_list

def shell_sort(my_list,sort_crit):
    elements = my_list['elements']
    size = my_list["size"]
    salto = size // 2
    
    if size<=1 or salto==0:
        return my_list
    while salto > 0:
        for i in range(salto,size):
            ancla = elements[i]
            control = i 
            while control >= salto and sort_crit(ancla,elements[control-salto]) == False:
                exchange(my_list,control,control-salto)
                control -= salto
        salto //= 2
    return my_list

def merge(lista1,lista2,sort_crit):
    lst = new_list()
    conteo1 = conteo2 = 0
    
    size1 = size(lista1)
    size2 = size(lista2)
    
    while size1>conteo1 and size2>conteo2:
        if sort_crit(get_element(lista1,conteo1),get_element(lista2,conteo2)):
            add_last(lst,get_element(lista1,conteo1))
            conteo1 +=1
        else:
            add_last(lst,get_element(lista2,conteo2))
            conteo2 +=1
    while conteo1 < size1:
        add_last(lst,get_element(lista1,conteo1))
        conteo1 +=1
    while conteo2 < size2:
        add_last(lst,get_element(lista2,conteo2))
        conteo2 +=1
    return lst

def merge_sort(my_list,sort_crit):
    
    elements = my_list['elements']
    size = my_list['size']
    
    if size<=1:
        return my_list
    
    split = size//2
    
    sublist1 = sub_list(my_list,0,split)
    sublist2 = sub_list(my_list,split,size-split)
    
    lista1 = merge_sort(sublist1,sort_crit)
    lista2 = merge_sort(sublist2,sort_crit)
    
    resultado = merge(lista1,lista2,sort_crit)
    
    my_list = resultado
    
    return my_list
    
    
def quick_sort(my_list,sort_crit):
    elements = my_list['elements']
    size = my_list['size']
    
    if size<=1:
        return my_list
    
    return quick_sorting(my_list,sort_crit,0,size-1)

def quick_sorting(my_list,sort_crit,low,high):
    if low < high:
        pivote = particion(my_list,low,high,sort_crit)
        quick_sorting(my_list,sort_crit,low,pivote-1)
        quick_sorting(my_list,sort_crit,pivote+1,high)
    return my_list
        
def particion(my_list,low,high,sort_crit):
    
    elements = my_list['elements']
    pivote = elements[high]
    low_nuevo = low - 1
    
    for j in range(low,high):
        if sort_crit(elements[j],pivote):
            low_nuevo += 1
            exchange(my_list,low_nuevo,j)
    exchange(my_list,low_nuevo+1,high)
    return low_nuevo + 1
    

    
    
    
>>>>>>> f4b03905d268e8c6705e3e8f394b6b37865d0a6f
