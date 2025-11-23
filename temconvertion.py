print("Choisissez le sens de conversion :")
print("1 - Celsius → Fahrenheit et Kelvin")
print("2 - Fahrenheit → Celsius et Kelvin")

choix = input("Votre choix (1 ou 2) : ")

if choix == "1":
    c = input("Entrez la température en Celsius : ")
    try:
        c = float(c)
        f = c * 9 / 5 + 32
        k = c + 273.15
        print(f"{c}°C = {f:.2f}°F = {k:.2f}K")
    except:
        print("Erreur : veuillez entrer un nombre valide.")

elif choix == "2":
    f = input("Entrez la température en Fahrenheit : ")
    try:
        f = float(f)
        c = (f - 32) * 5 / 9
        k = c + 273.15
        print(f"{f}°F = {c:.2f}°C = {k:.2f}K")
    except:
        print("Erreur : veuillez entrer un nombre valide.")

else:
    print("Choix invalide.")
