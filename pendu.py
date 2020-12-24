# Créé par Elève, le 19/12/2020 en Python 3.7

# on importe 'choice' pour choisir aléatoirement un mot parmi des listes de mots
from random import choice

####################
### Fonctions
####################


def choix_hasard():
    """
    Choisi un mot au hasard dans une liste prédéfinie
    :return: mot_choisi : str : mot choisi et à deviner par le joueur
    """
    # mots disponibles
    technologies = ["ordinateur", "souris", "clavier", "processeur", "ecran",
    "enceintes", "smartphone", "casque", "tablette", "drone", "windows"]

    fruits = ["framboise", "fraise", "pomme", "poire", "pamplemousse",
              "litchi", "orange", "mandarine", "banane", "raisin", "kiwi",
              "ananas", "cerise"]

    animaux = ["gazelle", "vache", "cheval", "pangolin", "zebre", "girafe",
               "ours", "tigre", "hippopotame", "lion", "ecureuil", "otarie",
               "elephant"]

    # choix du thème
    theme = input("Avec quel thème souhaitez-vous jouer ?\n\n1- Technologies" +
                  "\n2- Fruits\n3- Animaux\n4 -Revenir au menu")

    if theme == "1":
        mot_choisi = choice(technologies)

    elif theme == "2":
        mot_choisi = choice(fruits)

    elif theme == "3":
        mot_choisi = choice(animaux)

    elif theme == "4":  # revenir au menu
        raise NameError

    else:  # en cas d'erreur de saisie
        raise TypeError

    # postconditions
    assert type(mot_choisi) == str  # vérification type du mot

    return mot_choisi


def strAffiche(ch):
    """
    Renvoie le mot masqué
    :param: ch : str, mot à deviner
    :return: mot_affiche : str, mot choisi dont les lettres sont masquées
    """

    # préconditions
    assert type(ch) == str  # vérification du type de la variable

    mot_affiche = ""
    while len(ch) != len(mot_affiche):
        mot_affiche += "*"

    # postconditions
    assert len(ch) == len(mot_affiche)  # vérification longueur str

    return mot_affiche  # retour du mot masqué


def strReplace(ch1, ch2, lettre):
    """
    Remplace les "*" par des lettres si elles sont contenues dans le mot
    :param: ch1 : mot_choisi : str, c'est le mot à deviner
            ch2 : mot_affiche : str, c'est le mot masqué qui évolue
            lettre : str, proposée par le joueur
    :return: ch : str : mot masqué qui a peut être évolué
    """

    # vérification des types des variables
    assert type(ch1) == str and type(ch2) == str and type(lettre) == str

    liste_lettres = list(ch2)  # on transforme le mot masqué en une liste

    for i in range(len(ch1)):
        if ch1[i] == lettre:  # si la lettre est cotenue dans le mot
            liste_lettres[i] = lettre  # remplacement d'une "*" par la lettre
    ch = "".join(liste_lettres)  # on recolle les éléments de la liste en str

    # postconditions
    assert type(ch) == str
    assert len(ch) == len(ch1) == len(ch2)

    return ch  # retour du mot modifié


def menu():
    """
    Menu du jeu du pendu
    """

    print("**********************************************")
    print("Voici les règles du jeu :\n\n1- Vous disposez d'un nombre d'" +
          "essais limité défini par la taille du mot à deviner\n\n2- Vous" +
          "perdez un coup lorsque la lettre n'est pas présente dans le mot" +
          "ou si la lettre a déjà été saisie mais qu'elle n'est pas contenue" +
          ".Sinon, vous ne perdez pas de coups\n\n3- Les accents sont " +
          "comptés faux !")
    print("**********************************************")

    mot_choisi = choix_hasard()
    compteur = len(mot_choisi) + 1
    print("Compteur : ", compteur) ###NAME ERROR !!e!f
    coups = 0
    mot_affiche = strAffiche(mot_choisi)
    lettres_proposees = []

    while mot_affiche != mot_choisi and compteur != 0:
        print("\n-----------------------------")
        print("Mot inconnu :", mot_affiche)
        print("-----------------------------\n")
        print("Coup numéro :", coups)
        print("Lettres ou caractères déjà proposés :", lettres_proposees, "")
        print("Trouvez le mot en moins de ", compteur, "coups !\n\n")
        print("-------------------------------------------------------------")

        lettre = input("Saisir une lettre : ").lower()

        if lettre in mot_choisi:  # si la lettre est dans le mot choisi

            # si la lettre est contenue mais pas affichée
            if lettre not in mot_affiche:
                mot_affiche = strReplace(mot_choisi, mot_affiche, lettre)
                lettres_proposees.append(lettre)

            # si la lettre a déjà été saisie et qu'elle est affichée
            elif lettre in mot_affiche and lettre in lettres_proposees:
                print("Lettre déjà proposée et déjà remplacée dans le mot !")
            coups += 1


        elif lettre not in mot_choisi:  # si la lettre n'est pas dans le mot choisi

            if lettre in lettres_proposees:
                print("Lettre déjà proposée et non contenue dans le mot !!")

            else:
                print("Lettre ou caractère non contenu dans le mot !")

            coups += 1
            compteur -= 1
            lettres_proposees.append(lettre)

    if mot_affiche == mot_choisi:
        print("\n-----------------------------")
        print("Mot inconnu :", mot_affiche)
        print("-----------------------------\n")
        print("Bravo vous avez trouvé ! Le mot était : ", mot_choisi)

    else:
        print("Perdu ! le mot était : ", mot_choisi, "\nVous pouvez rejouer !")


###########################
### programme principal ###
###########################


continuer = True

while continuer:

    try:
        action = input("- Jeu du pendu -\n1- Jouer !\n2- Quitter\n")

        if action == "1":
            menu()

        elif action == "2":
            print("\nA bientôt pour de nouvelles parties endiablées !")
            continuer = False

        else:
            raise ValueError

    except ValueError:
        print("Merci de saisir des chiffres valides (1 ou 2) !")

    except AssertionError:
        print("Merci de saisir un chiffre valide !")

    except KeyboardInterrupt:
        print("Vous avez quitté le jeu ! A bientot !")
        continuer = False

    except NameError:
        pass

    except TypeError:
        print("Saisir un chiffre ! (1 ou 2 ou 3 ou 4)")

