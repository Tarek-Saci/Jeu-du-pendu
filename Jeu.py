
import random
def mot_aleatoire():
    with open("mots_pendu.txt", 'r') as s:
        s = s.read().split()
        i = random.randint(0,len(s)-1)     #indice aleatoire
        mot_aleatoir = str(s[i])
    return mot_aleatoir
#(_ _ _ _ _ )
def affichage (mot,lettre_utilisateur,mot_affiche):
    i = 0
    for i,lettre in enumerate(mot):
        if lettre_utilisateur == lettre:
            mot_affiche[i] = lettre_utilisateur

    #print(''.join(mot_affiche))
    return mot_affiche

run = True
# refaire une partie ?
score = 0

while run:  #passser a un aurtre mot
    nombre_vies = 6
    mot = mot_aleatoire()
    mot_affiche = ['_ '] * len(mot)
    lettre_utilisateur = ''


    while nombre_vies > 0 and mot_affiche.count('_ ') != 0: # Boucle du jeu

        print('veuillez entrer une lettre :')
        print(f'il vous reste {nombre_vies} chances')
        print(f'Score : {score}')
        affichage(mot,lettre_utilisateur,mot_affiche)
        print(''.join(mot_affiche))
        print(mot)
        if len(lettre_utilisateur) != 1:
            lettre_utilisateur=input()
            print('Une lettre a la fois')
            continue
        if lettre_utilisateur in mot:
            print('\n \n \n \n \n \n \n \nBravo ! vous avez trouvé une lettre !\n')
            lettre_utilisateur = ''

        else:
            nombre_vies = nombre_vies - 1
            print('\n \n \n \n \n \n \n \nce n\'est pas la bonne lettre')
            lettre_utilisateur = ''
    if mot_affiche.count('_ ') == 0:
        score = score + 1
        print(f'Vous avez trouvé le mot !\n {mot}')

    else:
        print(f'Vous avez perdu :\') \n Le mot etait {mot}\n votre score est : {score}')
        break

refaire = input('Voulez vous refaire une partie [y]/[n] ?\n')
if refaire == 'y':
    run = True
elif refaire == 'n':
    run = False
