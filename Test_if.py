login = "Admin"
PassW = "chaussette"
User = 0

print("\n")

if login == "Admin":
    if (PassW == "admin") or (PassW == "supermdp") or (PassW == "chaussette"):
        print("bienvenu", login,"!")
        User = 1
    else:
        print(login, ": Mot de passe invalide")
elif login == "rmechety":
    if PassW == "mdp":
        print("bienvenu", login,"!")
        User = 2
    else:
        print(login, ": Mot de passe invalide")
elif login == "JY":
    if PassW == "BG77540":
        print("bienvenu", login,"!")
        User = 3
    else:
        print(login, ": Mot de passe invalide")
else:
    print("ID inconnu")
    User = 0

print("Utilisateur n°", User, "\n")

try:
    pass
except