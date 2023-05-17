+import random
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
def mot_cache(a):
    liste1 = ['_ '] * len(a)
    print(''.join(liste1))
    return ''.join(liste1)
def affiche_lettre(lettre_utilisateur,mot):
    i = mot.find(lettre_utilisateur)

    print(mot_cache(mot))
    return

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
            affiche_lettre(lettre_utilisateur,mot)
            break
    refaire = input('voulez vous refaire une partie [y]/[n] ?\n')
    if refaire == 'y':
        run = True
    else:
        run = False
print(mot_aleatoire())