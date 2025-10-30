from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1

def rehash(my_map):
    capacidad_vieja = my_map["capacity"]
    capacidad_nueva = capacidad_vieja * 2
    if not mf.is_prime(capacidad_nueva):
        capacidad_nueva = mf.next_prime(capacidad_nueva)
        
    lst_nueva = lt.new_list()
    for i in range(0, capacidad_nueva):
        entrada = sl.new_list()
        lt.add_last(lst_nueva, entrada)
    
    lst_vieja = my_map["table"]  
    conteo = 0
    mapa_temporal_hash = {
                'prime': my_map['prime'],
                'capacity': capacidad_nueva,
                "scale":my_map['scale'],
                'shift':my_map['shift'],
            }
    
    for i in range(capacidad_vieja):
        lst_vieja = lt.get_element(my_map["table"], i)
        nodo = lst_vieja["first"]
        
        while nodo is not None:
            info = nodo["info"]
            key = me.get_key(info)
            
            hash = mf.hash_value(mapa_temporal_hash,key)
            
            bucket = lt.get_element(lst_nueva, hash)
            sl.add_last(bucket, info)
            
            nodo = nodo["next"]
            conteo += 1

    my_map["table"] = lst_nueva
    my_map["capacity"] = capacidad_nueva
    my_map["current_factor"] = conteo / capacidad_nueva
    my_map["size"] = conteo
    return my_map

def new_map(num_elements, load_factor, prime=109345121):
    
    capacidad = num_elements/load_factor
    if not mf.is_prime(capacidad):
        capacidad = mf.next_prime(capacidad)
        
    lst = lt.new_list()
    for i in range(capacidad):
        entrada = sl.new_list()
        lt.add_last(lst, entrada)
    
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

def put(my_map,key,value):
    
    hash = mf.hash_value(my_map,key)
    bucket = lt.get_element(my_map["table"],hash)
    
    nodo = bucket["first"]
    encontrado = False
    while nodo is not None and not encontrado:
        info = nodo["info"]
        if me.get_key(info) == key:
            nodo["info"] = me.new_map_entry(key,value)
            encontrado = True
        nodo = nodo["next"]
    
    if not encontrado:
        entrada = me.new_map_entry(key,value)
        sl.add_last(bucket, entrada)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        
        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)
    
    return my_map
    
def contains(my_map,key):
    
    hash = mf.hash_value(my_map,key)
    bucket = lt.get_element(my_map["table"],hash)
    
    nodo = bucket["first"]
    encontrado = False
    while nodo is not None and not encontrado:
        info = nodo["info"]
        if default_compare(key,info) == 0:
            encontrado = True
        nodo = nodo["next"]
    
    return encontrado

def get(my_map,key):
    
    hash = mf.hash_value(my_map,key)
    bucket = lt.get_element(my_map["table"],hash)
    
    nodo = bucket["first"]
    encontrado = False
    value = None
    while nodo is not None and not encontrado:
        info = nodo["info"]
        if default_compare(key,info) == 0:
            value = me.get_value(info)
            encontrado = True
        nodo = nodo["next"]
    
    return value

def remove(my_map, key):
    hash = mf.hash_value(my_map,key)
    bucket = lt.get_element(my_map["table"],hash)
    
    nodo = bucket["first"]
    encontrado = False
    conteo = 0
    while nodo is not None and not encontrado:
        info = nodo["info"]
        if default_compare(key,info) == 0:
            sl.delete_element(bucket, conteo)
            my_map["size"] -= 1
            my_map["current_factor"] = my_map["size"] / my_map["capacity"]
            encontrado = True
        nodo = nodo["next"]
        conteo +=1
    
    return my_map['table']
    
    
def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    if my_map["size"] == 0:
        return True
    return False

def key_set(my_map):
    keys = lt.new_list()
    tabla = my_map["table"]
    size = lt.size(tabla)
    for i in range(1, size):
        bucket = lt.get_element(tabla, i)
        nodo = bucket["first"]
        while nodo is not None:
            info = nodo["info"]
            key = me.get_key(info)
            lt.add_last(keys, key)
            nodo = nodo["next"]
    return keys

def value_set(my_map):
    values = lt.new_list()
    tabla = my_map["table"]
    size = lt.size(tabla)
    for i in range(1, size):
        bucket = lt.get_element(tabla, i)
        nodo = bucket["first"]
        while nodo is not None:
            info = nodo["info"]
            value = me.get_value(info)
            lt.add_last(values, value)
            nodo = nodo["next"]
    return values