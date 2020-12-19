# Créé par Elève, le 19/12/2020 en Python 3.7


####################
### Fonctions ######
####################


from random import choice

def strAffiche(ch):
    """
    Renvoie le mot masqué
    :param: ch : str, mot à deviner
    :return: str : mot_affiche, mot masqué
    """

    mot_affiche = ""
    while len(ch) != len(mot_affiche):
        mot_affiche += "*"
    return mot_affiche


def strReplace(ch1, ch2, lettre):
    """
    Remplace les "*" par des lettres
    :param: ch1 : str : mot_choisi, c'est le mot à deviner
            ch2 : str : mot_affiche, c'est le mot masqué qui évolue
            lettre : str : lettre saisie par l'utilisateur
    :return: ch : str : mot masqué a évolué
    """

    liste_lettres = list(ch2)
    for i in range(len(ch1)):
        if ch1[i] == lettre:
            liste_lettres[i] = lettre
    ch = "".join(liste_lettres)
    return ch


###########################
### programme principal ###
###########################

mot_choisi = "chaise"
mot_affiche = strAffiche(mot_choisi)

compteur = 10

while mot_affiche != mot_choisi:

    lettre = input("Saisir une lettre :")

    if lettre in mot_choisi:
        mot_affiche = strReplace(mot_choisi, mot_affiche, lettre)
        compteur -= 1

    elif lettre not in mot_choisi:
        print("Lettre non contenue dans le mot !")
        compteur -= 1

    print(mot_affiche)













