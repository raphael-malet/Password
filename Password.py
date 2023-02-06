#password

import re
import hashlib
import json


def verification_condition(mot_de_passe):
    mdp = mot_de_passe
    if len(mdp) < 8:
        return False
    if not bool(re.search("[a-z]", mdp)):
        return False
    if not bool(re.search("[A-Z]", mdp)):
        return False
    if not bool(re.search("[0-9]", mdp)):
        return False
    if not bool(re.search("[!@?,;*)(°§€#$%^&*./+=@#&:;]", mdp)):
        return False
    else:
        return True


def mdp_existant(mot_de_passe, mot_de_passe_crypte):
    mdp_crypte = mot_de_passe_crypte
    fichier = open('stockage_mdp.txt', 'r')
    liste_mdp = fichier.read()
    fichier.close()
    liste_mdp = json.loads(liste_mdp)
    if mot_de_passe in liste_mdp:
        print('mots de passe deja utiliser')
        return False
    else:
        fichier_ecriture = open('stockage_mdp.txt', 'w')
        liste_mdp.update({mot_de_passe: mdp_crypte})
        liste_mdp = json.dumps(liste_mdp)
        fichier_ecriture.write(liste_mdp)
        fichier_ecriture.close()
        return True


def cryptage(mot_de_passe):
    mdp = mot_de_passe
    mdp_encode = mdp.encode()
    crypt = hashlib.sha256(mdp_encode)
    mdp_crypte = crypt.hexdigest()
    print(mdp_crypte)
    if mdp_existant(mdp, mdp_crypte):
        return True
    else:
        print('votre mot de passe est deja utiliser')
        return False


def afficher_mot_de_passe():
    fichier = open('stockage_mdp.txt', 'r')
    afficher_mdp = fichier.read()
    fichier.close()
    afficher_mdp = json.loads(afficher_mdp)
    for i in afficher_mdp:
        print(i + '      ' + afficher_mdp.get(i))


def menu():
    while True:
        choix = input('Entrez :\n 1. Entrer nouveaux mot de passe\n 2.afficher mot de passe\n')
        if choix == '1':
            while True:
                mdp = input('Entrer mots de passe avec minimum 8 caractère, 1 majuscule, 1 caractère spéciale :\n ')
                verification_condition(mdp)
                if verification_condition(mdp):
                    if cryptage(mdp):
                        print('mot de passe enregistré')
                        break
                else:
                    print('les conditions ne sont pas remplis, veuillez réessayer.')
        if choix == '2':
            afficher_mot_de_passe()


menu()
