# Créé par Elève, le 19/12/2020 en Python 3.7

from random import choice  # on importe 'choice' pour choisir aléatoirement un mot parmi une liste de mots

####################
### Fonctions
####################

def choix_hasard():
    """Choisi un mot au hasard dans une liste prédéfinie
    :return: mot_choisi : str : mot à deviner
    """
    fichier = open("technologies.txt", "r")
    lignes = fichier.readlines()
    for ligne in lignes:

        a = choice(lignes)

    liste_eclattee = list(a)

    liste_eclattee.pop()
    liste_eclattee.pop()

    mot_choisi = "".join(liste_eclattee)

    return mot_choisi


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
    Remplace les "*" par des lettres si elles sont contenues dans le mot
    :param: ch1 : str : mot_choisi, c'est le mot à deviner
            ch2 : str : mot_affiche, c'est le mot masqué qui évolue
            lettre : str : lettre saisie par l'utilisateur
    :return: ch : str : mot masqué qui a peut être évolué
    """

    liste_lettres = list(ch2)  # on transforme le mot masqué en une liste

    for i in range(len(ch1)):
        if ch1[i] == lettre:  # si la lettre est cotenue dans le mot
            liste_lettres[i] = lettre  # remplacement d'une "*" par la lettre
    ch = "".join(liste_lettres)  # on recolle les éléments de la liste en une str
    return ch  # retour du mot modifié


def menu(action):
    """
    Menu du jeu du pendu
    :param: action : str : action que l'utilisateur souhaite effectuer
    """


    # préconditions

    # on vérifie que le chiffre associé à l'action est valide
    assert action == "1" or action == "2"



    while action != "2":

        if action == "1":

            mot_choisi = choix_hasard()
            mot_affiche = strAffiche(mot_choisi)

            compteur = 10
            lettres_proposees = []

            while mot_affiche != mot_choisi:

                lettre = input("\nSaisir une lettre : ")

                # si la lettre est contenue mais pas affichée
                if lettre in mot_choisi and lettre not in mot_affiche:
                    mot_affiche = strReplace(mot_choisi, mot_affiche, lettre)
                    compteur -= 1
                    lettres_proposees.append(lettre)

                # si la lettre a déjà été saisie mais qu'elle n'est pas contenue
                elif lettre in lettres_proposees and lettre not in mot_choisi:
                    print("Lettre déjà proposée !")
                    compteur -= 1

                # si la lettre a déjà été saisie et qu'elle est affichée
                elif lettre in lettres_proposees and lettre in mot_affiche:
                    print("Lettre déjà proposée et déjà remplacée dans le mot !")

                # si la lettre n'est pas contenue
                elif lettre not in mot_choisi:
                    print("Lettre non contenue dans le mot !")
                    compteur -= 1
                    lettres_proposees.append(lettre)


                print("Coup numéro :", compteur)
                print("Mot inconnu", mot_affiche)
                print("Lettres déjà proposées :", lettres_proposees, "\n")


###########################
### programme principal ###
###########################


continuer = True

while continuer != False:

    try:

        action = input("\nBonjour bienvenue sur notre jeu !\n1- Jouer !\n2- Quitter ")
        menu(action)

    except AssertionError:
        print("Merci de saisir un chiffre valide !")

    except KeyboardInterrupt:
        print("Vous avez quitté le jeu ! A bientot !")
        continuer = False











