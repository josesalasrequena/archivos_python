# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open('stock.csv','r')
    ferreteria = list(csv.DictReader(csvfile))
    cantidad_tornillos = 0
    cantidad_tuercas = 0
    cantidad_arandelas = 0

    for i in range(len(ferreteria)):
        articulos = ferreteria [i]
        for k,v in articulos.items():
            if k == 'tornillos':
                cantidad_tornillos += int(v)
            elif k == 'tuercas':
                cantidad_tuercas += int(v)
            else:
                cantidad_arandelas += int(v)
    print('La cantidad de tornillos es:', cantidad_tornillos, 'La cantidad de tuercas es:', cantidad_tuercas,
    'La cantidad de arandelas es:', cantidad_arandelas)
    csvfile.close()


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    csvfile = open('propiedades.csv','r')     
    propiedades = list(csv.DictReader(csvfile))
    sin_ambient = 0
    dos_ambient = 0
    tres_ambient = 0
    error = 0
    for i in range(len(propiedades)):       
       dpto = propiedades[i]
       for k,v in dpto.items():
          try:
              ambientes = int(v)
              if ambientes == 2:
                dos_ambient += int(v)
              elif ambientes == 3:
                tres_ambient += int(v)
              elif ambientes == " ":
                error += int(v)
              else:
                sin_ambient += int(v)
          except:
            print("Existen Departamentos que no tienen suficiente informacion")          
    print("Departamentos de dos ambientes:",dos_ambient)
    print("Departamentos de tres ambientes:",tres_ambient)
    print("Departamentos sin informacion:",error)
    print('Departamentos con error en informacion:',sin_ambient)
   
    csvfile.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
