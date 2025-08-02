
estudiantes=[]
try:
    cantidad_estudiantes= int(input("Ingrese cantidad de estudiantes a ingresar:"))
except ValueError:
    print("Error: Ingrese números validos...")
else:
    for i in range(cantidad_estudiantes):
        notas_1=[]
        notas=0
        nombre= input("ingrese nombre de estudiante:").lower()

        cantidad_notas= int(input("Ingrese cantidad de notas:"))
        print("Error: Deben ser numeros validos.")

        for notas_estudiantes in range(cantidad_notas):
            print(f"Nota{notas_estudiantes +1}")
            nota= int(input(f"Ingrese nota {notas_estudiantes+1}"))
            notas_1.append(nota)
            notas += nota

        promedio = notas/len(notas_1)
        estudiantes.append([nombre,promedio])

    for student in estudiantes:
        print(f"{student[0]} tiene el promedio de {student[1]}")