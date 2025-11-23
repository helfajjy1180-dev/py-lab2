a=float(input("donner le 1 nombre :"))
b=float(input("donner le 1 nombre :"))
print("choisis votre chiox :")
print("1 : addition")
print("2 : soustraction")
print("3 : multuplication")
print("4 : division")
choix=input("donner votr choix :")
if choix == "1":
        resultat = a + b
        print(f"{a} + {b} = {resultat}")
else:       
    if choix == "2":
        resultat = a - b
        print(f"{a} - {b} = {resultat}")
    else:
        if choix== "3":
           resultat = a * b
           print(f"{a} * {b} = {resultat}")
        else:
            if choix == "4":
               if b == 0:
                 print("Erreur : division par zéro impossible.")
            else:
                resultat = a / b
                print(f"{a} / {b} = {resultat}")
