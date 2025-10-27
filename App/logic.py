"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """

import csv
import time
import os

# TODO Realice la importación de priority queue
# TODO Realice la importación de ArrayList (al) o SingleLinked (sl) como estructura de datos auxiliar para sus requerimientos


data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'


def new_logic():
    """ Inicializa el analizador

   stops: Tabla de hash para guardar los vertices del grafo
   connections: Grafo para representar las rutas entre estaciones
   components: Almacena la informacion de los componentes conectados
   paths: Estructura que almancena los caminos de costo minimo desde un
           vertice determinado a todos los otros vértices del grafo
    """
    analyzer = {
        'stops': None,
        'routes_pq': None
    }
    
    analyzer['stops'] = None #TODO completar la creación de la lista
    analyzer['routes_pq'] = None #TODO completar la creación de la cola de prioridad

    return analyzer

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def load_data(analyzer, file):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    file = data_dir + file
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for stop in input_file:
        add_stop(analyzer, stop)
    return analyzer


def add_stop(analyzer, stop):
    """
    Adiciona una parada al analizador
    """
    al.add_last(analyzer['stops'], stop)
    # TODO Adicionar nuevo elemento a la cola de prioridad
    return analyzer


# ___________________________________________________
#  Funciones de consulta
# ___________________________________________________

def stops_size(analyzer):
    """
    Obtener el número de paradas de bus
    """
    return al.size(analyzer['stops'])

def pq_size(analyzer):
    """
    Obtener el número de elementos en la cola de prioridad
    """
    return pq.size(analyzer['routes_pq'])

def pq_first(analyzer):
    """
    Obtener el primer elemento en la cola de prioridad
    """
    return pq.get_first_priority(analyzer['routes_pq'])

def get_next_route(analyzer):
    """
    Retorna la ruta con mayor prioridad
    """
    # TODO completar la función
    pass 
