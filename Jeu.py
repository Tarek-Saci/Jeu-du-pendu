
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
while run:# refaire une partie ?
    nombre_vies = 6
    mot = mot_aleatoire()
    mot_affiche = ['_ '] * len(mot)
    lettre_utilisateur = ''

    while nombre_vies > 0: # Boucle du jeu
        print('veuillez entrer une lettre :')
        print(f'il vous reste {nombre_vies} chances')
        affichage(mot,lettre_utilisateur,mot_affiche)
        print(mot_affiche)
        print(mot)
        if len(lettre_utilisateur) != 1:
            lettre_utilisateur=input()
            continue
        if lettre_utilisateur in mot:
            print('Bravo ! vous avez trouvé une lettre !')
            lettre_utilisateur = ''

        else:
            nombre_vies = nombre_vies - 1
            print('ce n\'est pas la bonne lettre')


    refaire = input('voulez vous refaire une partie [y]/[n] ?\n')
    if refaire == 'y':
        run = True
    else:
        run = False
