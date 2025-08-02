
estudiantes=[]
try:
    cantidad_estudiantes= int(input("Ingrese cantidad de estudiantes a ingresar:"))
except ValueError:
    print("Error: Ingrese números validos...")
else:
    for i in range(cantidad_estudiantes):
        notas_1=[]
        notas=0
        try:
            nombre= input("ingrese nombre de estudiante:").lower()
            cantidad_notas= int(input("Ingrese cantidad de notas:"))

            for notas_estudiantes in range(cantidad_notas):
                try:
                    print(f"Nota{notas_estudiantes +1}")
                    nota= int(input(f"Ingrese nota {notas_estudiantes+1}"))
                except ValueError:
                    print("Error: Ingrese datos validos..")
                else:
                    notas_1.append(nota)
                    notas += nota

            promedio = notas/len(notas_1)
            estudiantes.append([nombre,promedio])
        except ValueError:
            print("Error: Debe ingresar números validos...")
        except Exception as e:
            print("Se produjo un error inesperado",e)

    for student in estudiantes:
        print(f"{student[0]} tiene el promedio de {student[1]}")