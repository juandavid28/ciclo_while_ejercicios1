#Ejemplo de un Menu

num = int(input("Menu: 1(ver numeros), 0(Salir) "))
while num != 0:

    x =0
    while x < 10:
        print("El valor de X es: ",x)
        x += 1

    print("Saliendo,,,")
    num = int(input("Menu: 1(ver numeros), 0(Salir) "))

print("Gracias")