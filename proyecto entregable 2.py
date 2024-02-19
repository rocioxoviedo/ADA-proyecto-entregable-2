# -*- coding: utf-8 -*-
import os
class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def obtener_nombre(self):
        return self.__nombre

class CatalogoPelicula:
    def __init__(self, nombre_catalogo):
        self.nombre = nombre_catalogo
        self.ruta_archivo = f"{nombre_catalogo}.txt"
        self.__crear_archivo_si_no_existe()
        
    def __crear_archivo_si_no_existe(self):
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'a') as archivo:
                archivo.write("")
    
    def agregar_pelicula(self, nombre_pelicula):
        with open(self.ruta_archivo, 'w') as archivo:
            archivo.write(f"{nombre_pelicula}\n")
            
    def listar_peliculas(self):
        if not os.path.exists(self.ruta_archivo):
            print("¡Ups! Este catálogo no tiene ninguna película.")
            return
        
        with open(self.ruta_archivo, 'r') as archivo:
            print("Las películas en este catálogo son:")
            for linea in archivo:
                print(linea.strip())
                
    def eliminar_catalogo(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print("El catálogo de películas se eliminó.")
        else:
            print("¡Ups! El catálogo de películas no existe.")
    
def main():
    nombre_catalogo = input("Ingresá el nombre del catálogo de películas: ")
    catalogo = CatalogoPelicula(nombre_catalogo)
    
    while True:
        print("\nOpciones: ")
        print("1. Agregar una película")
        print("2. Listar películas")
        print("3. Eliminar el catálogo")
        print("4. Salir")
        
        opcion = input("Ingresá una opción:")
        
        if opcion == "1":
            nombre_pelicula = input("Ingresá el nombre de la película que quieras agregar: ")
            catalogo.agregar_pelicula(nombre_pelicula)
            
        elif opcion == "2":
            catalogo.listar_peliculas()
        
        elif opcion == "3":
            catalogo.eliminar_catalogo()
            break
        
        elif opcion == "4":
            print("Gracias por usar el programa ¡Hasta pronto!")
            break
        
        else:
            print("Opción inválida. Por favor, intentalo de nuevo.")

if __name__ == "__main__":
    main()