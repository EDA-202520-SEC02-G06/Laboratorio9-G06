from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def is_available(table, pos):

   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def new_map(num_elements, load_factor,prime=109345121):
    
    lst = lt.new_list()
    for i in range(0, num_elements):
        entry = me.new_map_entry(None, None)
        lt.add_last(lst, entry)

    capacidad = num_elements/load_factor
    if not mf.is_prime(capacidad):
        capacidad = mf.next_prime(capacidad)  
    scale = 1
    shift = 0
    
    my_table = {
        'prime': prime,
        'capacity': capacidad,
        "scale":scale,
        "shift":shift,
        "table": lst,
        'current_factor':0,
        'limit_factor':load_factor,
        'size':0
    }
    return my_table

def rehash(my_map):
    capacidad_vieja = my_map["capacity"]
    capacidad_nueva = capacidad_vieja * 2
    if not mf.is_prime(capacidad_nueva):
        capacidad_nueva = mf.next_prime(capacidad_nueva)

    tabla_vieja = my_map["table"]
    size_viejo = my_map["size"]
    tabla_nueva = lt.new_list()
    for i in range(0, size_viejo):
        dato = lt.get_element(tabla_vieja, i)
        lt.add_last(tabla_nueva, dato)
    
    size = lt.size(tabla_nueva)
    my_map["size"] = size
    my_map["capacity"] = capacidad_nueva
    my_map["table"] = tabla_nueva
    return my_map


def put(my_map,key,value):
    
    hash = mf.hash_value(my_map,key)
    tabla = my_map["table"]['elements']
    ocupied, slot = find_slot(my_map,key,hash)
    datos = me.new_map_entry(key,value)
    if not ocupied:
        lt.change_info(my_map["table"],slot,datos)
        my_map["size"] += 1
    else:
        lt.change_info(my_map["table"],slot,datos)
        my_map["size"] += 1
        
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)
    return my_map

def contains(my_map,key):
    hash = mf.hash_value(my_map,key)
    tabla = my_map["table"]
    ocupied, slot = find_slot(my_map,key,hash)
    if ocupied:
        return True
    return False

def get(my_map,key):
    hash = mf.hash_value(my_map,key)
    ocupied, slot = find_slot(my_map,key,hash)
    if ocupied:
        entry = lt.get_element(my_map['table'], slot)
        return me.get_value(entry)
    return None

def remove(my_map, key):
   hash_value = mf.hash_value(my_map, key)
   ocupied, slot = find_slot(my_map, key, hash_value)
   if ocupied:
      entry = lt.get_element(my_map['table'], slot)
      me.set_key(entry, '__EMPTY__')
      me.set_value(entry, '__EMPTY__')
      my_map['size'] -= 1
   return my_map['table']

def size(my_map):
   return my_map['size']

def is_empty(my_map):
    if my_map['size'] == 0:
        return True
    return False

def key_set(my_map):
    keys = lt.new_list()
    tabla = my_map["table"]
    size = lt.size(tabla)
    
    for i in range(size):
        dato = lt.get_element(tabla, i)
        key = me.get_key(dato)
        if key is not None and key != "__EMPTY__":
            lt.add_last(keys, key)
    return keys

def value_set(my_map):
    values = lt.new_list()
    tabla = my_map["table"]
    size = lt.size(tabla)
    
    for i in range(size):
        dato = lt.get_element(tabla, i)
        value = me.get_value(dato)
        if value is not None and value != "__EMPTY__":
            lt.add_last(values, value)
    return values



    