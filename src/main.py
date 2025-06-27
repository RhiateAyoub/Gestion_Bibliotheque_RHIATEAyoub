import re
from bibliotheque import *
from visualisations import *

def menu():
    print("=== GESTION BIBLIOTHEQUE ===")
    print("  1. Ajouter un livre")
    print("  2. Inscrire un membre")
    print("  3. Emprunter un livre")
    print("  4. Rendre un livre")
    print("  5. Lister tous les livres")
    print("  6. Lister tous les membres")
    print("  7. Afficher les statistiques")
    print("  8. Sauvegarder et quitter")

# Validation des champs:
def saisir_non_vide(prompt):
    while True:
        valeur = input(prompt).strip()
        if valeur:
            return valeur
        raise SaisieInvalideError("Ce champ ne peut pas être vide.")

# Validation de l'année:
def valider_annee(prompt):
    while True:
        annee = int(saisir_non_vide(prompt))
        if annee <= 0:
            raise SaisieInvalideError("L'année ne peut pas être négative.")
        return annee

def valider_id(prompt):
    while True:
        id = saisir_non_vide(prompt)
        if not id.isdigit():
            raise SaisieInvalideError("L'ID doit contenir seulement des chiffres.")
        return id

def valider_isbn(prompt):
    while True:
        isbn = saisir_non_vide(prompt)
        if re.fullmatch(r"97[89][-\d]{10,16}", isbn):
            return isbn
        raise SaisieInvalideError("ISBN Invalide. Exemple de format accepté: 978-0-306-40615-7")

biblio = Bibliotheque()
biblio.charger()

while True:
    try:
        menu()
        choix = input("Votre choix: ")
        match choix:
            # 1. Ajouter un livre ---------------------
            case "1":
                titre = saisir_non_vide("Titre: ")
                auteur = saisir_non_vide("Auteur: ")
                isbn = valider_isbn("ISBN: ")
                annee = valider_annee("Année: ")
                genre = saisir_non_vide("Genre: ")
                livre = Livre(isbn, titre, auteur, annee, genre)
                biblio.ajouter_livre(livre)
                print("Livre ajouté avec succès!")
            # 2. Inscrire un membre ---------------------
            case "2":
                id_membre = valider_id("ID membre: ")
                nom = saisir_non_vide("Nom: ")
                biblio.ajouter_membre(Membre(id_membre, nom))
                print("Membre inscrit avec succès!")
            # 3. Emprunter un livre ---------------------
            case "3":
                id_membre = valider_id("ID membre: ")
                titre = saisir_non_vide("Titre: ")
                biblio.emprunter_livre(id_membre, titre)
                print("Livre emprunté avec succès! ID Membre: ", id_membre)
            # 4. Rendre un livre ---------------------
            case "4":
                id_membre = valider_id("ID membre: ")
                titre = saisir_non_vide("Titre: ")
                biblio.rendre_livre(id_membre, titre)
                print("Livre rendu avec succès! ID Membre: ", id_membre)
            # 5. Lister tous les livres ---------------------
            case "5":
                print("---------- Liste des livres ----------\n" + biblio.lister_livres())
            # 6. Lister tous les membres ---------------------
            case "6":
                print("---------- Liste des membres ----------\n" + biblio.lister_membres())
            # 7. Afficher les statistiques ---------------------
            case "7":
                while True:
                    print("---- Visualisations ----")
                    print("-- 1. Répartition des livres par genre")
                    print("-- 2. Top N auteurs les plus populaires")
                    print("-- 3. Activité des emprunts (30 derniers jours)")
                    choix = input("Votre choix: ")
                    match choix:
                        case "1":
                            print("Visualisation de la répartition des livres par genre...")
                            diagramme_genres(biblio.livres)
                            break
                        case "2":
                            top = input("Donner N (le nombre des auteurs): ")
                            print(f"Visualisation de Top {top} auteurs les plus populaires...")
                            top_auteurs(biblio.livres, 10)
                            break
                        case "3":
                            print("Visualisatoin de l'activité des emprunts...")
                            activite_emprunts("data/historique.csv")
                            break
                        case _:
                            print("Option invalide! Veuillez entrer 1,2 ou 3.")
            # 8. Sauvegarder et quitter ---------------------
            case "8":
                biblio.sauvegarder()
                print("Données sauvegardées. À bientôt !")
                break
    except Exception as e:
        print(f"Erreur: {e}")
