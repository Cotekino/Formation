login = "JY"
PassW = "BG77540"

print("\n")

if login == "Admin":
    if PassW == "admin":
        print("bienvenu ", login," !")
    else:
        print(login, ": Mot de passe invalide")
elif login == "rmechety":
    if PassW == "mdp":
        print("bienvenu ", login," !")
    else:
        print(login, ": Mot de passe invalide")
elif login == "JY":
    if PassW == "BG77540":
        print("bienvenu ", login," !")
    else:
        print(login, ": Mot de passe invalide")
else:
    print("ID inconnu")

print("\n")
