lista_alumnos=[]

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