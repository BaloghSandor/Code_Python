#Code fait par Sandor Balogh, Gr : 403
#Date : 2022-09-25
#On crée une fonction qu'on appelle 'count_word' pour demander à l'utilisateur d'entrer une pharse afin de lui montrer
#le nombre de qu'il y avait dans cette phrase avec les fonctions : len(), input(), str() et print() :

def count_word():
   words = input('Bonjour, veuillez entrer quelque chose et je vais compter le nombre de mots : ')
   print('\nLe nombre de mots dans votre phrase est de : ' + str(len(words.split(" "))))

count_word()