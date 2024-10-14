# """
# - Registar alumnos.
# - Generar fichas de matricula.
# - Mostrar la lista de todos los matriculados.
# - Filtrar matriculados por programa de estudios.
# """


# cantidad_alumnos = int(input("¿Cuántos alumnos deseas ingresar? "))
# lista_alumnos = []
# for i in range(cantidad_alumnos):
#     nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
#     lista_alumnos.append(nombre)
# print("Lista de alumnos ingresada:", lista_alumnos)


# lista_alumnos=[]
# while True:
#     opcion=input("""Elije lo que decea hacer
#         escribe (s) si decea registrar un alumno
#         escrbe (n) si desea salir del programa
#         escribe tu respuersta: """)
#     if opcion.lower=="n":
#         break
#     nombre=input("ingrese el ombre del alumno: ")
#     apellido=input("ingrese apellido del alumno: ")

#     alumno={
#         "nombre":nombre,
#         "apellido":apellido
#     }
# lista_alumnos.append(alumno)
# print(lista_alumnos)

# |----------------------------------------------------------ejemplo realizado en el salon-------------------------------------------------------------|
lista_alumnos=[]

def mensaje_menu():
    menu_opciones=("""  
    -------------biembenido al sistema---------------
        ----------registra tu alumno------------
    1. escribe (s) si desea agregar un numevo alumno:
    2. escribe (n) si desea salir del programa:
    escribe la accion que desea realizar
    """)
    return menu_opciones

def ingresar_datos_alumno():
    id=len(lista_alumnos)+1
    print(id)
    cui=int(input("ingrese su numero de dni: "))
    nombre=input("ingrese el nombre de su alumno: ")
    apellido=input("ingrese el apellido de su alumno: ")
    celular=int(input("ingrese su telefono: "))
    programa_estudios=input("ingrese su programa de estudio: ")
    ciclo_academico=input("ingrese su ciclo academico:")
    email=input("ingrece su correo electronico:")
    guardar_datos_alumno(id,cui,nombre,apellido,celular,programa_estudios,ciclo_academico,email)

def guardar_datos_alumno(id,cui,nombre,apellido,celular,programa_estudios,ciclo_academico,email):
    alumno={
        "id":id,
        "cui":cui,
        "nombre":nombre,
        "apellio":apellido,
        "celular":celular,
        "programa_estudios":programa_estudios,
        "ciclo_academico":ciclo_academico,
        "email":email
        }
    lista_alumnos.append(alumno)

while True:
    menu_opciones=input(mensaje_menu())
    if menu_opciones.lower()=="n":
        print("saliendo del sistema")
        break

    elif menu_opciones.lower()=="s":
        ingresar_datos_alumno()

    else:
        print("opcion erronea")

print(lista_alumnos)