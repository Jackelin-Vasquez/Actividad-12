notas_1= []
notas=0
try:
    cantidad_estudiantes= int(input("Ingrese cantidad de estudiantes a ingresar:"))
except ValueError:
    print("Error: Ingrese números validos...")

for i in range(cantidad_estudiantes):
    try:
        nombre= input("ingrese nombre de estudiante:").lower()
    except ValueError:
        print("Error: deben ser valores validos.")

        cantidad_notas= int(input("Ingrese cantidad de notas:"))
    except ValueError:
        print("Error: Deben ser numeros validos.")

    for notas in range(cantidad_notas):
        print(f"Nota{notas +1}")
        nota= int(input(f"Ingrese nota {notas+1}"))
        notas_1.append(nota)
        nota += notas

        promedio = notas/len(notas)

print(f"{nombre} tiene un promedio de {promedio}")