from bibliotheque import *

def menu():
    print("1. Ajouter un livre")
    print("2. Inscrire un membre")
    print("3. Emprunter un livre")
    print("4. Sauvegarder et quitter")

biblio = Bibliotheque()
biblio.charger()

while True:
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
            biblio.sauvegarder()
            print("Données sauvegardées. À bientôt !")
            break
