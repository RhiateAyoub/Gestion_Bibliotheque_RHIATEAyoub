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

biblio = Bibliotheque()
biblio.charger()

while True:
    try:
        menu()
        choix = input("Votre choix: ")
        match choix:
            case "1":
                titre = input("Titre: ")
                auteur = input("Auteur: ")
                isbn = input("ISBN: ")
                annee = int(input("Année: "))
                genre = input("Genre: ")
                livre = Livre(isbn, titre, auteur, annee, genre)
                biblio.ajouter_livre(livre)
                print("Livre ajouté avec succès!")
            case "2":
                id_membre = input("ID membre: ")
                nom = input("Nom: ")
                biblio.ajouter_membre(Membre(id_membre, nom))
                print("Membre inscrit avec succès!")
            case "3":
                id_membre = input("ID membre: ")
                titre = input("Titre: ")
                biblio.emprunter_livre(id_membre, titre)
                print("Livre emprunté avec succès! ID Membre: ", id_membre)
            case "4":
                id_membre = input("ID membre: ")
                titre = input("Titre: ")
                biblio.rendre_livre(id_membre, titre)
                print("Livre rendu avec succès! ID Membre: ", id_membre)
            case "5":
                print("---------- Liste des livres ----------\n" + biblio.lister_livres())
            case "6":
                print("---------- Liste des membres ----------\n" + biblio.lister_membres())
            case "7":
                print("---- Visualisations ----")
                print("-- 1. Répartition des livres par genre")
                print("-- 2. Top N auteurs les plus populaires")
                print("-- 3. Activité des emprunts (30 derniers jours)")
                choix = input("Votre choix: ")
                match choix:
                    case "1":
                        print("Visualisation de la répartition des livres par genre...")
                        diagramme_genres(biblio.livres)
                    case "2":
                        top = input("Donner N (le nombre des auteurs): ")
                        print(f"Visualisation de Top {top} auteurs les plus populaires...")
                        top_auteurs(biblio.livres, 10)
                    case "3":
                        print("Visualisatoin de l'activité des emprunts...")
                        activite_emprunts("data/historique.csv")
            case "8":
                biblio.sauvegarder()
                print("Données sauvegardées. À bientôt !")
                break
    except Exception as e:
        print(f"Erreur: {e}")
