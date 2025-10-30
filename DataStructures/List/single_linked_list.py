def new_list():
    newlist = {
        'first': None,
        'last': None,
        'size': 0,
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node['info']

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list['first']
    count = 0
    
    while not is_in_array and temp is not None:
        if cmp_function(element, temp['info']) == 0:
            is_in_array = True
        else:
            temp = temp['next']
            count += 1
    if not is_in_array:
        count = -1
    return count

def add_first(my_list,element):
    
    new_list_node = {
        'info': element,
        'next' : None
    }
    
    if my_list['size'] == 0:
        my_list['first'] = new_list_node
        my_list['last'] = new_list_node
        
    else:
        new_list_node['next'] = my_list['first']
        my_list['first'] = new_list_node
        
    my_list['size'] += 1
    
    return my_list

def add_last(my_list, element):
    
    new_list_node = {
        'info': element,
        'next' : None
    }
    
    if my_list['size'] == 0:
        my_list['first'] = new_list_node
        my_list['last'] = new_list_node
        my_list['size'] += 1
        return my_list
    
    else:
        my_list['last']['next'] = new_list_node
        my_list['last'] = new_list_node
        my_list['size'] += 1
        return my_list

def size(my_list):
    return my_list['size']

def first_element(my_list):
    if my_list['size'] == 0:
        return None
    else:
        return my_list['first']['info']
    
def is_empty(my_list):
    if my_list['size'] == 0:
        return True
    else:
        return False

def last_element(my_list):
    if my_list['size'] == 0:
        return None
    else:
        return my_list['last']['info']
    
def delete_element(my_list, pos):
    if pos < 0 or pos > my_list['size']:
        return my_list
    counter = 0
    cur = my_list['first']
    prev = None
    while cur != None:
        if counter == pos:
            if prev == None:
                my_list['first'] = cur['next']
            elif cur['next'] == None:
                my_list['last'] = prev
                prev['next'] = None
            else:
                prev['next'] = cur['next']
            my_list['size'] -= 1
            break
        prev = cur
        cur = cur['next']
        counter += 1
    return my_list

def remove_first(my_list):
    removed = my_list['first']['info']
    if my_list['size'] == 0:
        return 'IndexError: list index out of range'
    else:
        my_list['first'] = my_list['first']['next']
        my_list['size'] -= 1
        return removed
    
def remove_last(my_list):
    removed = my_list['last']['info']
    if my_list['size'] == 0:
        return 'IndexError: list index out of range'
    elif my_list['size'] == 1:
        my_list['first'] = None
        my_list['last'] = None
        my_list['size'] -= 1
        return removed
    else:
        cur = my_list['first']
        prev = None
        while cur['next'] != None:
            prev = cur
            cur = cur['next']
        prev['next'] = None
        my_list['last'] = prev
        my_list['size'] -= 1
        return removed
    
def insert_element(my_list, pos, element):
    if pos < 0 or pos > my_list['size']:
        return my_list
    
    new_list_node = {
        'info': element,
        'next' : None
    }
    
    if pos == 0:
        new_list_node['next'] = my_list['first']
        my_list['first'] = new_list_node
        if my_list['size'] == 0:
            my_list['last'] = new_list_node
    elif pos == my_list['size']:
        my_list['last']['next'] = new_list_node
        my_list['last'] = new_list_node
    else:
        counter = 0
        cur = my_list['first']
        prev = None
        while cur != None:
            if counter == pos:
                prev['next'] = new_list_node
                new_list_node['next'] = cur
                break
            prev = cur
            cur = cur['next']
            counter += 1
            
    my_list['size'] += 1
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list['size'] or pos2 < 0 or pos2 >= my_list['size'] or pos1 == pos2:
        return my_list
    
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    
    counter = 0
    cur = my_list['first']
    node1 = None
    node2 = None
    
    while cur != None:
        if counter == pos1:
            node1 = cur
        if counter == pos2:
            node2 = cur
            break
        cur = cur['next']
        counter += 1
    
    if node1 is not None and node2 is not None:
        node1['info'], node2['info'] = node2['info'], node1['info']
    
    return my_list

def sub_list(my_list, start_pos, end_pos):
    if start_pos < 0 or end_pos >= my_list['size'] or start_pos > end_pos:
        return None
    
    new_sublist = new_list()
    counter = 0
    cur = my_list['first']
    
    while cur != None:
        if counter >= start_pos and counter <= end_pos:
            add_last(new_sublist, cur['info'])
        if counter > end_pos:
            break
        cur = cur['next']
        counter += 1
    
    return new_sublist  

def change_info(my_list, pos, new_element):
    if pos < 0 or pos >= my_list['size']:
        return my_list
    
    counter = 0
    cur = my_list['first']
    
    while cur != None:
        if counter == pos:
            cur['info'] = new_element
            break
        cur = cur['next']
        counter += 1
    
    return my_list

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_crit):
    size = my_list['size']
    if size <= 1:
        return my_list

    for i in range(size-1):
        indice_minimo = i
        for j in range(i+1, size):
            if not sort_crit(get_element(my_list, j), get_element(my_list, indice_minimo)):
                indice_minimo = j
        if indice_minimo != i:
            exchange(my_list, i, indice_minimo)
    return my_list

def insertion_sort(my_list, sort_crit):
    size = my_list['size']
    if size <= 1:
        return my_list
    
    tail_sorted = my_list['first']
    cur = tail_sorted['next']
    
    while cur is not None:
        valor = cur['info']
        next_cur = cur['next']
        
        if sort_crit(valor, tail_sorted['info']):
            tail_sorted['next'] = next_cur
            cur['next'] = my_list['first']
            my_list['first'] = cur
            if next_cur is None:
                my_list['last'] = tail_sorted
        else:
            pivote = my_list['first']
            while pivote['next'] is not None and sort_crit(valor, pivote['next']['info']):
                pivote = pivote['next']
            if pivote == tail_sorted:
                tail_sorted = cur
            else:
                tail_sorted['next'] = next_cur
                cur['next'] = pivote['next']
                pivote['next'] = cur
                if next_cur is None:
                    my_list['last'] = tail_sorted
        cur = next_cur
    return my_list
    
def shell_sort(my_list,sort_crit):
    size = my_list['size']
    salto = size//2
    
    if size<=1 or salto==0:
        return my_list
    
    while salto > 0:
        for i in range(salto,size):
            ancla = get_element(my_list,i)
            control = i
            while control >= salto and (not sort_crit(ancla,get_element(my_list,(control-salto)))):
                exchange(my_list,control,control-salto)
                control-=salto
        salto //=2
    return my_list


def merge_sort(my_list, sort_crit):
    if my_list['size'] <= 1:
        return my_list
    mid = my_list['size'] // 2
    left = sub_list(my_list, 0, mid - 1)
    right = sub_list(my_list, mid, my_list['size'] - 1)

    left = merge_sort(left, sort_crit)
    right = merge_sort(right, sort_crit)

    return merge(left, right, sort_crit)

def merge(left, right, sort_crit):
    result = new_list()  
    i = 0
    j = 0
    while i < left['size'] and j < right['size']:
        e1 = get_element(left, i)
        e2 = get_element(right, j)
        if sort_crit(e1, e2):
            add_last(result, e1)
            i += 1
        else:
            add_last(result, e2)
            j += 1
    while i < left['size']:
        add_last(result, get_element(left, i))
        i += 1
    while j < right['size']:
        add_last(result, get_element(right, j))
        j += 1
    return result

def quick_sort(my_list, sort_crit):
    if my_list['size'] <= 1:
        return my_list

    pivot_value = first_element(my_list)

    menores = new_list()
    mayores = new_list()

    current = my_list['first']['next']
    while current is not None:
        value = current['info']
        if sort_crit(value, pivot_value):
            add_last(menores, value)
        else:
            add_last(mayores, value)
        current = current['next']

    menores = quick_sort(menores, sort_crit)
    mayores = quick_sort(mayores, sort_crit)

    return concatenate_quick(menores, pivot_value, mayores)


def concatenate_quick(left_list, pivot_value, right_list):
    
    result = new_list()
    current = left_list['first']
    while current is not None:
        add_last(result, current['info'])
        current = current['next']

    add_last(result, pivot_value)

    current = right_list['first']
    while current is not None:
        add_last(result, current['info'])
        current = current['next']

    return result 