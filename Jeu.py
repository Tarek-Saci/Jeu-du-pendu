import random

# Ne prend rien en entree,lis le fichier mot_pendu.txt, donne en sortie une liste de mots
def bank_mot():
    with open("mots_pendu.txt",'r') as s:
        return s.read().split()
# ne prend rien en entre, appele la fonction bank_mot extrait un mot aleatoir, donne en sortie une chaine de caracteres
def mot_aleatoire():
    i = random.randint(0,len(bank_mot())-1)      #indice aleatoire
    mot_aleatoir = str(bank_mot()[i])
    return mot_aleatoir
#(_ _ _ _ _ )
def affichage (lettre_utilisateur,mot,tirets):
    tirets[mot.find(lettre_utilisateur)] = lettre_utilisateur
    #print(''.join(tirets))
    print (tirets)
    return
def tirets(mot):
    tirets = [' _'] * len(mot)
    return tirets

run = True
while run:# refaire une partie ?
    nombre_vies = 6
    mot = mot_aleatoire()
    while nombre_vies > 0: # Boucle du jeu
        print('veuillez entrer une lettre :')
        mot_cache(mot)
        print(f'il vous reste {nombre_vies} chances')
        print(mot)
        lettre_utilisateur=input()
        if lettre_utilisateur in mot:

            continue
        else:
            nombre_vies = nombre_vies - 1
    refaire = input('voulez vous refaire une partie [y]/[n] ?\n')
    if refaire == 'y':
        run = True
    else:
        run = False
print(mot_aleatoire())