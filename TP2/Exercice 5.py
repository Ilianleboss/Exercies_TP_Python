nombre=int(input("Entrez un nombre entier : "))

if nombre % 2 == 0 or nombre % 2 == 2:
    if nombre >= 0:
        print("Le nombre est positif et pair")
    else:
        print("Le nombre est negatif et pair")
else:
    if nombre >= 0:
        print("Le nombre est positif et impair")
    else:
        print("Le nombre est negatif et impair")