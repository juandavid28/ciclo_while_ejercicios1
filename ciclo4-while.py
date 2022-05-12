#ejercicio4

num = int(input("Escribe un numero positivo "))
while num < 0:
    print("Este es un numero negativo, prueva de nuevo")
    num = int(input("Escribe un numero positivo "))
print ("el numero es: ", num)