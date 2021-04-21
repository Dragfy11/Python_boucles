# importation du randint
from random import randint
#JEU DU JUSTE PRIX

#choisir un nombre entre 1 et 1000
prix = randint(1, 1000)

#statut du jeu (activé/désactivé)
run = True
#tant que le jeu n'est pas fini
while run:

#-> demander à l'utilisateur "entrer un prix"
    userprice = int(input("Entrer un prix: "))
#-> si il trouve le juste prix "c'est gagné ! "
    if userprice == prix:
        print("c'est gagné !")
        run = False
#->sinon on affiche "c'est moins" ou "c'est plus"
    elif userprice > prix:
        print("c'est moins")
    elif userprice < prix:
        print("c'est plus")
# fin du jeu
print("fin du jeu")


