# Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
# recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
import os
from turtle import clear

# Primera ficha

print("Bienvenido al programa.\n")
a, b = map(int, input("Ingrese dos numeros pertenecientes a su primera ficha, separados por un espacio. Para salir ingrese dos ceros: ").split())
while(a != 0 or b != 0):
    centinela = 0
    fichaUno = []
    fichaDos = []
    
    while(a < 0 or a > 6 or b < 0 or b > 6):
        print("Numeros invalidos. Solo numeros enteros positivos.")
        a, b = map(int, input("Ingrese dos numeros pertenecientes a su primera ficha, separados por un espacio: ").split())
    fichaUno.append(a)
    fichaUno.append(b)

    # Segunda ficha

    c, d = map(int, input("Ahora ingrese dos numeros pertenecientes a su segunda ficha, separados por un espacio: ").split())
    while(c < 0 or c > 6 or d < 0 or d > 6):
        print("Numeros invalidos. Solo numeros enteros positivos.")
        c, d = map(int, input("Ingrese dos numeros pertenecientes a su segunda ficha, separados por un espacio: ").split())
    fichaDos.append(c)
    fichaDos.append(d)

    # Comparacion

    for i in(fichaUno):
        if i in fichaDos:
            centinela = 1
            break

    # Resultado

    if(centinela == 1):
        print("Las fichas encajan.")
    else:
        print("Las fichas no encajan.")
        
    # Repregunta la condicion del ciclo
    os.system('pause')
    os.system('cls')
    a, b = map(int, input("Ingrese dos numeros pertenecientes a su primera ficha, separados por un espacio. Para salir ingrese dos ceros: ").split())

print("FIN")

    