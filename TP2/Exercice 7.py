import random

nombre = random.randint(0, 74)
print("Nombre tire :", nombre)

if nombre < 50:
    print("Pile !")
else:
    print("Face !")