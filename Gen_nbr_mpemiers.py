
liste_des_num_premier = []
total = 20
nombre_a_tester = 2

import math

def est_premier(n):
    for diviseur in range( 2 , int(math.sqrt(n))+1 ):
        if n%diviseur == 0:   # trouvé un diviseur
            return False
    return True

#fichier_sortie = open('Prime_NBR_database', 'w') 

while len(liste_des_num_premier) < total:    # faut en trouver 100...
    
    if est_premier(nombre_a_tester):
        liste_des_num_premier.append(nombre_a_tester)  #inseré dans la liste
        print(f'{nombre_a_tester} est premier !')
    else:
        print(f'{nombre_a_tester}')
    
    nombre_a_tester += 1   # on passe au suivant.

#fichier_sortie.close()
