import datetime

age = int(input("Donnez votre age : "))
annee = datetime.datetime.now().year - age

print("Votre annee de naissance est :", annee)