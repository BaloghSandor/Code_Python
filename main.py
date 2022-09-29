from random import randint

boucle_jeu = True
valeur_cherche = randint(1,10)

while boucle_jeu:
   print('Bonjour, je vais choisir un nombre entre 0 et 100 et vous devez le deviner \n')
   input_1 = int(input('Donnez votre première essaie : '))

   if input_1 == valeur_cherche:
       print('Bravo! Vous avez réussi!\n')
       recommencer = input('Voulez vous recommencer (répondez par oui ou non)? ')

       if recommencer == 'oui':
           continue
       elif recommencer == 'non':
           break

   elif input_1 < valeur_cherche:
       print('Oups! Vous avez eu tort! Le nombre que vous cherché est plus petit que ',input_1)
       input_2 = int(input('Donnez votre deuxième essaie : '))

       if input_2 ==

   else:
       print('Oups! Vous avez eu tort! Le nombre que vous cherché est plus grand que ', input_1)


