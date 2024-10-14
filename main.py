"""
- Registar alumnos.
- Generar fichas de matricula.
- Mostrar la lista de todos los matriculados.
- Filtrar matriculados por programa de estudios.
"""
lista_alumnos = []
while True:
    nombre = input("Ingresa el nombre del alumno (o escribe 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    lista_alumnos.append(nombre)
print("Lista de alumnos ingresada:", lista_alumnos)

# alumnos={}

# print(lista_alumnos)

cantidad_alumnos = int(input("¿Cuántos alumnos deseas ingresar? "))
lista_alumnos = []
for i in range(cantidad_alumnos):
    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
    lista_alumnos.append(nombre)
print("Lista de alumnos ingresada:", lista_alumnos)


lista_alumnos=[]
while True:
    opcion=input("""Elije lo que decea hacer
        escribe (s) si decea registrar un alumno
        escrbe (n) si desea salir del programa
        escribe tu respuersta: """)
    if opcion.lower=="n":
        break
    nombre=input("ingrese el ombre del alumno: ")
    apellido=input("ingrese apellido del alumno: ")

    alumno={
        "nombre":nombre,
        "apellido":apellido
    }
lista_alumnos.append(alumno)
print(lista_alumnos)