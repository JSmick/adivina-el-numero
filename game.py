import random
import time

number_random = random.randint(1, 100)

print("Generando numero")
for i in range(3):
    time.sleep(1)
    print(".")
    
print("Numero Generado exitosamente!")
print(number_random)

while True:
    number_by_user = input("Ingrese un numero del 1 al 100\n---> ")
    if number_by_user == str(number_random):
        print("¡Hurra! Has adivinado el numero")
        break
    else:
        print("Intentelo de nuevo\n\n")
