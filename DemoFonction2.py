
def est_autorise_a_conduire(age,etat_permis):
    return age >= 18 and etat_permis == True

def est_autorise_a_passer_permis(age,etat_permis):
    return etat_permis == False and age >= 16


def traitement(valeur_age,etat_permis):
    if valeur_age < 18:
        print("Attendre 1 annee")
        valeur_age += 1
    if est_autorise_a_passer_permis(valeur_age,etat_permis):
        print("Passage du permis")
        etat_permis = True
    return valeur_age,etat_permis,"coucou"

age = 10
permis = False
message = ""

while not est_autorise_a_conduire(age,permis):
    age,permis,message = traitement(age,permis)
    print(f"---AGE:{age}--Permis:{permis} ---- MSG:{message}")
