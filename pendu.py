# Créé par Elève, le 19/12/2020 en Python 3.7

# on importe 'choice' pour choisir aléatoirement un mot parmi une liste de mots
from random import choice

####################
### Fonctions
####################


def choix_hasard():
    """Choisi un mot au hasard dans une liste prédéfinie
    :return: mot_choisi : str : mot à deviner
    """
    # ---- fonctionne uniquement avec le fichier texte correspondant ---------
    #fichier = open("technologies.txt", "r")
    #lignes = fichier.readlines()
    #for ligne in lignes:
    #    mot = choice(lignes)

    #liste_eclatee = list(mot)

    #del liste_eclatee[-2:]
    #mot_choisi = "".join(liste_eclatee)
    # ------------------------------------------------------------------------

    technologies = ["ordinateur", "souris", "clavier", "processeur", "ecran", "enceintes", "smartphone", "casque", "tablette", "drone", "windows"]
    fruits = ["framboise", "fraise", "pomme", "poire", "pamplemousse", "litchi", "orange", "mandarine", "banane", "raisin", "kiwi", "ananas", "cerise"]
    animaux = ["gazelle", "vache", "cheval", "pangolin", "zebre", "girafe", "ours", "tigre", "hippopotame", "lion", "ecureuil", "otarie", "elephant"]

    theme = input("Avec quel thème souhaitez-vous jouer ?\n\n1- Technologies" +
                  "\n2- Fruits\n3- Animaux\n4 -Revenir au menu")

    if theme == "1":
        mot_choisi = choice(technologies)

    elif theme == "2":
        mot_choisi = choice(fruits)

    elif theme == "3":
        mot_choisi = choice(animaux)

    elif theme == "4":
        raise NameError

    else:
        raise TypeError

    # postconditions
    assert type(mot_choisi) == str

    return mot_choisi


def strAffiche(ch):
    """
    Renvoie le mot masqué
    :param: ch : str, mot à deviner
    :return: str : mot_affiche, mot masqué
    """

    # préconditions
    assert type(ch) == str

    mot_affiche = ""
    while len(ch) != len(mot_affiche):
        mot_affiche += "*"

    # postconditions
    assert len(ch) == len(mot_affiche)  # vérification longueur str

    return mot_affiche  # retour du mot masqué


def strReplace(ch1, ch2, lettre):
    """
    Remplace les "*" par des lettres si elles sont contenues dans le mot
    :param: ch1 : str : mot_choisi, c'est le mot à deviner
            ch2 : str : mot_affiche, c'est le mot masqué qui évolue
            lettre : str : lettre saisie par l'utilisateur
    :return: ch : str : mot masqué qui a peut être évolué
    """

    assert type(ch1) == str and type(ch2) == str and type(lettre) == str

    liste_lettres = list(ch2)  # on transforme le mot masqué en une liste

    for i in range(len(ch1)):
        if ch1[i] == lettre:  # si la lettre est cotenue dans le mot
            liste_lettres[i] = lettre  # remplacement d'une "*" par la lettre
    ch = "".join(liste_lettres)  # on recolle les éléments de la liste en str

    assert type(ch) == str

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
    coups = len(mot_choisi) + 1
    compteur = len(mot_choisi) + 1
    COUPS = 0
    mot_affiche = strAffiche(mot_choisi)
    propositions = []

    while mot_affiche != mot_choisi and compteur != 0:
        print("\n-----------------------------")
        print("Mot inconnu", mot_affiche)
        print("-----------------------------\n")
        print("Coup numéro :", COUPS)
        print("Il vous reste :", compteur, "coups")
        print("Lettres ou caractères déjà proposés :", propositions, "")
        print("Il faut trouver le mot en moins de ", coups, "coups !\n\n")
        print("-------------------------------------------------------------")

        lettre = input("Saisir une lettre : ").lower()

        if lettre in mot_choisi:

            # si la lettre est contenue mais pas affichée
            if lettre in mot_choisi and lettre not in mot_affiche:
                mot_affiche = strReplace(mot_choisi, mot_affiche, lettre)
                propositions.append(lettre)
                COUPS += 1

            # si la lettre a déjà été saisie mais qu'elle n'est pas contenue
            elif lettre in propositions and lettre not in mot_choisi:
                print("Lettre déjà proposée !")
                compteur -= 1
                COUPS += 1

            # si la lettre a déjà été saisie et qu'elle est affichée
            elif lettre in propositions and lettre in mot_affiche:
                print("Lettre déjà proposée et déjà remplacée dans le mot !")

            # si la lettre n'est pas contenue
            elif lettre not in mot_choisi:
                print("Lettre non contenue dans le mot !")
                compteur -= 1
                propositions.append(lettre)
                COUPS += 1

        elif lettre not in propositions:
            print("Lettre ou caractère non contenu dans le mot !")
            propositions.append(lettre)
            compteur -= 1
            COUPS += 1

    if mot_affiche == mot_choisi:
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

    except AssertionError:
        print("Merci de saisir un chiffre valide !")

    except KeyboardInterrupt:
        print("Vous avez quitté le jeu ! A bientot !")
        continuer = False

    except ValueError:
        print("Merci de saisir des chiffres valides (1 ou 2) !")

    except TypeError:
        print("Saisir un chiffre ! (1 ou 2 ou 3 ou 4)")

    except NameError:
        pass
