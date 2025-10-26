import sys
import App.logic as logic
# TODO Realice la importación de lista como estructura de datos auxiliar para la presentación de los resultados

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""
#  -------------------------------------------------------------
# Funciones para la carga de datos
#  -------------------------------------------------------------

def new_logic():
    """
    Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control


# ___________________________________________________
#  Menu principal
# ___________________________________________________

def print_menu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de buses de singapur")
    print("3- Consultar las n rutas de bus con mayor prioridad")
    print("4- Consultar las paradas de la ruta con la n-esima prioridad")
    print("0- Salir")
    print("*******************************************")

"""
Menu principal
"""

def main():
    working = True
    routesfile = 'bus_routes_14000.csv'
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n>')

        if int(inputs[0]) == 1:
            print("\nInicializando....")
            control = new_logic()
        elif int(inputs[0]) == 2:
            print("\nCargando información de crimenes ....")
            logic.load_data(control, routesfile)
            print('Registros cargados: ' + str(logic.stops_size(control)))
            print('Rutas cargadas: ' + str(logic.routes_size(control)))
            print('Elementos en la cola de prioridad: ' + str(logic.pq_size(control)))
        elif int(inputs[0]) == 3:
            print("\nBuscando rutas con mayor prioridad: ")
            numRoutes = int(input("Cantidad de rutas a consultar: "))
            total, routes = logic.get_routes(control, numRoutes)
            print("\nTotal de rutas: " + str(total))
            for route in range(0, al.size(routes)):
                print("Ruta: " + al.get_element(routes, route))
        elif int(inputs[0]) == 4:
            print("\nBuscando las paradas de la n-esima ruta con mayor prioridad: ")
            pos = int(input("Valor de n: "))
            route, stops = logic.get_stops_by_route(control, pos)
            print(f"\nRuta con la {pos}-esima prioridad: " + str(route))
            for stop in range(0, al.size(stops)):
                print("Parada: " + al.get_element(stops, stop))
        else:
            sys.exit(0)
    sys.exit(0)
