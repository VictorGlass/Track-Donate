#Bienvenido a Track Donate - Sistema de Donacion de Organos.

#En su primera instancia procedemos a realizar la importacion de la libreria
#NumPy para poder trabaja con las matrices y operaciones numericas.
import numpy as np

#Desde el modulo collections importamos la clase defaultdict, la cual
#se utilizara para agrupar a los pacientes por grupo sanguineo de manera
#mas eficiente.
from collections import defaultdict


#Creamos y definimos una clase llamada DonacionOrganos.
class DonacionOrganos:


#Realizamos la creacion de una matriz tipo Numpy la cual esta vacia, y esta
#se utilizará para almacenar los datos del paciente.

#Como se puede observar tiene un valor que comienza en 0 hasta 6, esto 
#quiere decir que tendra 6 columnas para cada atributo del paciente.
    def __init__(self):
        self.pacientes = np.empty((0, 6), dtype=object)



#La funcion mostrar_menu imprime las opciones del menu para que el usuario
#pueda interactuar con el sistema.
    def mostrar_menu(self):
        print("\nBienvenido a Track Donate")
        print("Sistema de Donacion de Organos")
        print("\n")
        print("1. Agregar Paciente")
        print("2. Ver Pacientes")
        print("3. Comparar Compatibilidad entre 2 Pacientes")
        print("4. Optimizar Donación")
        print("5. Sumatoria de Teléfonos por Grupo Sanguíneo")
        print("6. Sucesión de Cantidad de Pacientes por Grupo Sanguíneo")
        print("7. Salir")



#La funcion agregar_paciente le solicita al usuario que ingrese los datos
#necesarios del paciente para ser ingresado al sistema, los cuales luego
#pasaran a la matriz self.pacientes para ser almacenados.
    def agregar_paciente(self):
        print("\nIngrese los datos del paciente: ")
        rut, nombre, apellido, telefono, direccion, grupo_sanguineo = input("RUT: "), input("Nombre: "), input("Apellido: "), input("Teléfono: "), input("Dirección: "), input("Grupo Sanguíneo (A, B, AB, O): ")

        paciente = np.array([[rut, nombre, apellido, telefono, direccion, grupo_sanguineo]])
        self.pacientes = np.vstack((self.pacientes, paciente))
        print("Paciente agregado con éxito.")



#la funcion ver_pacientes imprimira por consola una lista de los pacientes
#mostrando los encabezados y los detalles de los mismos de cada paciente que
#ha sido ingresado.
    def ver_pacientes(self):
        print("\nLista de Pacientes: ")
        header = ["RUT", "Nombre", "Apellido", "Teléfono", "Dirección", "Grupo Sanguíneo"]
        print("\t".join(header))
        for paciente in self.pacientes:
            print("\t".join(map(str, paciente)))



#La funcion de calcular_compatibilidad determina la compatibilidad entre dos grupos
#sanguineos utilizando una logica simplificada que se basa en reglas de compatibilidad
#aceptadas en la medicina.

#Por ejemplo:
#Si ambos gupos sanguineos son iguales osea compatibles, la funcion 
#devolvera un puntaje de compatibilidad de '1.0', osea compatibilidad total.
    def calcular_compatibilidad(self, grupo1, grupo2):
        if grupo1 == grupo2:
            return 1.0
        elif grupo1 == "AB" or grupo2 == "AB":
            return 0.75
        elif (grupo1 == "A" and grupo2 == "B") or (grupo1 == "B" and grupo2 == "A"):
            return 0.5
        elif grupo1 == "O" or grupo2 == "O":
            return 0.25
        else:
            return 0.0



#La funcion comparar_compatibilidad permite al usuario seleccionar 2 pacientes
#para luego poder calcular y mostrar la compatibilidad entre sus grupos sanguineos
    def comparar_compatibilidad(self):
        print("\nSeleccione dos pacientes para comparar la compatibilidad: ")
        self.ver_pacientes()
        index1 = int(input("Ingrese el índice del primer paciente: "))
        index2 = int(input("Ingrese el índice del segundo paciente: "))

        if 0 <= index1 < len(self.pacientes) and 0 <= index2 < len(self.pacientes):
            paciente1, paciente2 = self.pacientes[index1], self.pacientes[index2]
            compatibilidad = self.calcular_compatibilidad(paciente1[5], paciente2[5])
            print(f"\nCompatibilidad entre {paciente1[1]} y {paciente2[1]}: {compatibilidad}")
        else:
            print("Índices de pacientes no válidos.")



#La funcion optimizar_pacientes logra agrupar por grupo sanguineo a los pacientes
#utilizando un diccionario 'grupos_sanguineos'. Esto luego imprimira la cantidad
#de pacientes en cada grupo sanguineo.
    def optimizar_donacion(self):
        grupos_sanguineos = defaultdict(list)
        for paciente in self.pacientes:
            grupos_sanguineos[paciente[5]].append(paciente)

        print("\nOptimización de donación: ")
        for grupo, pacientes_grupo in grupos_sanguineos.items():
            print(f"Grupo Sanguíneo {grupo}: {len(pacientes_grupo)} pacientes")

            for i in range(len(pacientes_grupo)):
                for j in range(i + 1, len(pacientes_grupo)):
                    paciente1, paciente2 = pacientes_grupo[i], pacientes_grupo[j]
                    compatibilidad = self.calcular_compatibilidad(paciente1[5], paciente2[5])
                    print(f"  - Compatibilidad entre {paciente1[1]} y {paciente2[1]}: {compatibilidad}")



#La funcion sumatoria tiene como fin calcular la sumatoria de los numeros de
#telefono para cada grupo sanguineo y muestra su resultado.
    def sumatoria_telefonos_por_grupo_sanguineo(self):
        grupos_sanguineos = defaultdict(int)
        for paciente in self.pacientes:
            grupos_sanguineos[paciente[5]] += int(paciente[3])

        print("\nSumatoria de Teléfonos por Grupo Sanguíneo: ")
        for grupo, sumatoria in grupos_sanguineos.items():
            print(f"Grupo Sanguíneo {grupo}: {sumatoria}")



#La funcion sucesion cuenta la cantidad de pacientes por grupo sanguineo y
#nos muestra el resultado.
    def sucesion_cantidad_pacientes(self):
        grupos_sanguineos = defaultdict(int)
        for paciente in self.pacientes:
            grupos_sanguineos[paciente[5]] += 1

        print("\nSucesión de Cantidad de Pacientes por Grupo Sanguíneo: ")
        for grupo, cantidad in grupos_sanguineos.items():
            print(f"Grupo Sanguíneo {grupo}: {cantidad}")


#La funcion ejecutar se encarga de iniciar la ejecucion del programa
#mostrando el menu y generando las acciones segun la opcion que haya seleccionado
#el usuario.
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("\nSeleccione una opción (1-7): ")

            if opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.ver_pacientes()
            elif opcion == "3":
                self.comparar_compatibilidad()
            elif opcion == "4":
                self.optimizar_donacion()
            elif opcion == "5":
                self.sumatoria_telefonos_por_grupo_sanguineo()
            elif opcion == "6":
                self.sucesion_cantidad_pacientes()
            elif opcion == "7":
                print("Gracias por utilizar Track Donate")
                print("Un Sistema de Donacion de Organos")
                print("Hasta Luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")



#Este bloque if verificara que se este ejecutando el script directamente y no
#importando como un modulo.
if __name__ == "__main__":
    sistema_donacion = DonacionOrganos()
    sistema_donacion.ejecutar()

#En general, el programa se ejecutara en un bucle infinito, que mostrara el menu
#y realizara acciones segun lo que ingrese el usuario.

#Cada opcion del menu correspondera con un metodo especifico de la clase 
#que creamos llamada DonacionOrganos.