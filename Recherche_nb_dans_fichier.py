
import time

# demander un nombre 1..100
nombre_choisi_str = input("lequel ? \(1..100\)")
try:
    nombre_choisi = int(nombre_choisi_str)
except:
    print("pas valide")
    exit
"""   if nombre_choisi < 1 or nombre_choisi >100:
        raise ValueError   """

if nombre_choisi < 1:
    print(f'Trop bas; nombre considéré: 1')
    nombre_choisi = 1
if nombre_choisi > 100:
    print(f'Trop haut; nombre considéré: 100')
    nombre_choisi = 100

# ouvrir fichier
fichier_a_lire = open('Prime_NBR_database', 'r')

# lire fichier entier dans une liste (fichier pas très grand...)
liste_ligne_DB = fichier_a_lire.readlines()

# chercher l'element selon l'index (lire la n-ème ligne)
Nb_premier_cherche = liste_ligne_DB[nombre_choisi-1]
Nb_premier_cherche = Nb_premier_cherche.strip()

# print ligne trouvée
print(f'Le nombre premier cherché est:')
time.sleep(1)
print(f' {Nb_premier_cherche} !\n')

# fermer fichier
fichier_a_lire.close()