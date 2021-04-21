# for : pour une valeur de départ (1) jusque -> (∞)
#for client in range(1, 6):
 #   print("vous êtes le client n°", client)

# for each : pour chaque valeur d'une liste données
#lister les emails
#mail= ["dragfy@hotmail.com", "dragfy@dragfy.yt", "dragfy@dragfy", "d@d", "contact@dragfy.yt"]

#blacklist
#blacklist = ["dragfy@dragfy", "d@d"]

#pour chaqu'une des valeurs, j'affiche "Email envoyé à [inserer l'email]
#for mails in mail:
 #   print("Email envoyé à :", mails)

#blacklist
#for mails in mail:
 #   if mails in blacklist:
  #      print("Email {} interdit ! envoi impossible...".format(mails))
   #     continue
    #print("Email envoyé à :", mails)

# while : tant qu'un condition est vrai
# salarié 1500€ / mois
#salary = 1500

# tant que  salaire < 2000€, + 120€
#while salary < 2000:
    #ajouter 120 € au salaire
    #salary += 120
    #print("votre salaire actuel est de {} €".format(salary))

#print("fin du programme")

#un dev "Dragfy", 2500 abonnés
suscribe = 2500

#il gagne 10 % d'audience supplementaire par mois
month = 0

#on souhaite estimer, combien aura t'il d'abonnés, après 2 ans (24mois)
while month <=24:

    #augmenter l'audience
    suscribe *= 1.10

    #afficher le nombre d'abonnés
    print("vous avez actuellement {} abonnés !".format(suscribe))

    #on passe au mois suivant
    month+=1

