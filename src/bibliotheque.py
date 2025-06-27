import json
import os
from exceptions import *
import csv
from datetime import datetime

# --------------------- Classe Livre ---------------------
class Livre:
    def __init__(self, isbn, titre, auteur, annee, genre, disponible=True):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre
        self.disponible = disponible

    def __str__(self):
        return (
            f"Titre : {self.titre}\n"
            f"-- Auteur : {self.auteur}\n"
            f"-- ISBN : {self.isbn}\n"
            f"-- Genre : {self.genre}\n"
            f"-- Année : {self.annee}\n"
            f"-- Disponible : {self.disponible}\n"
        )

    def emprunter(self):
        if self.disponible:
            self.disponible = False
        else:
            raise LivreIndisponibleError()

    def rendre(self):
        if not self.disponible:
            self.disponible = True
        else:
            raise LivreIndisponibleError("Le livre n'est pas emprunté ligne 35.")

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titre": self.titre,
            "auteur": self.auteur,
            "annee": self.annee,
            "genre": self.genre,
            "disponible": self.disponible
        }

    @staticmethod
    def from_dict(data): # Méthode statique qui ne dépend pas de l'instance
        return Livre(
            isbn = data["isbn"],
            titre = data["titre"],
            auteur = data["auteur"],
            annee = data["annee"],
            genre = data["genre"],
            disponible = data["disponible"]
        )


# --------------------- Classe Membre ---------------------
class Membre:
    def __init__(self, id_membre, nom):
        self.id_membre = id_membre
        self.nom = nom
        self.livres_empruntes = []

    def __str__(self):
        return (
            f"Nom: {self.nom}\n"
            f"ID: {self.id_membre}\n"
            f"Livres empruntés: {[livre.isbn for livre in self.livres_empruntes]}\n"
        )

    def emprunter_livre(self, livre:Livre):
        # Un membre ne peut pas emprunter plus de 3 livres en même temps:
        if len(self.livres_empruntes) >= 3:
            raise QuotaEmpruntDepasseError()
        if livre.disponible:
            livre.emprunter()
            self.livres_empruntes.append(livre)
        else:
            raise LivreIndisponibleError()

    def rendre_livre(self, livre:Livre):
        if not livre.disponible:
            livre.rendre()
            self.livres_empruntes = [l for l in self.livres_empruntes if l.isbn != livre.isbn]
        else:
            raise LivreIndisponibleError("Le livre n'est pas emprunté.")

    def to_dict(self):
        return {
            "id_membre": self.id_membre,
            "nom": self.nom,
            "livres_empruntes": [livre.isbn for livre in self.livres_empruntes]
        }

    @staticmethod
    def from_dict(data, livres): # Méthode statique qui ne dépend pas de l'instance
        membre = Membre(data["id_membre"], data["nom"])
        # Actualiser la liste avec les ISBN des livres:
        isbn_empruntes = data.get("livres_empruntes", [])
        membre.livres_empruntes = [livre for livre in livres if livre.isbn in isbn_empruntes]
        return membre
            

# --------------------- Classe Bibliotheque ---------------------
class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.membres= []

    def lister_livres(self):
        if not self.livres:
            return "Aucun livre enregistré dans la bibliothèque."
        
        # Utilisation de __str__ pour afficher les données de chaque livre
        res = ""
        for livre in self.livres:
            res += str(livre) + "\n"
        return res
    
    def lister_membres(self):
        if not self.membres:
            return "Aucun membre est inscrit dans la bibliothèque."
        
        # Utilisation de __str__ pour afficher les données de chaque membre
        res = ""
        for membre in self.membres:
            res += str(membre) + "\n"
        return res

    def ajouter_livre(self, livre:Livre):
        self.livres.append(livre)

    def ajouter_membre(self, membre:Membre):
        self.membres.append(membre)
        
    def emprunter_livre(self, id_membre, titre_livre):
        mbr = None
        lvr = None

        # Chercher le membre correspondat au id saisi
        for membre in self.membres:
            if membre.id_membre == id_membre:
                mbr = membre
                break
        if mbr is None:
            raise MembreInexistantError()
        
        # Chercher le livre correspondant au titre saisi
        for livre in self.livres:
            if livre.titre == titre_livre:
                lvr = livre
                break
        if lvr is None:
            raise LivreInexistantError()
        mbr.emprunter_livre(lvr)
        enregistrer_action(mbr.id_membre, lvr.isbn, "emprunt")

    def rendre_livre(self, id_membre, titre_livre):
        mbr = None
        lvr = None
        # Chercher le membre correspondat au id saisi
        for membre in self.membres:
            if membre.id_membre == id_membre:
                mbr = membre
                break
        if mbr is None:
            raise MembreInexistantError()
        # Chercher le livre correspondant au titre saisi
        for livre in mbr.livres_empruntes:
            if livre.titre == titre_livre:
                lvr = livre
                break
        if lvr is None:
            raise LivreInexistantError("Ce membre n'a pas emprunté ce livre!")
        mbr.rendre_livre(lvr)

    # Sauvegarder et charger les données des fichiers json
    def sauvegarder(self):
        with open("data/livres.json", "w", encoding="utf-8") as f:
            json.dump([livre.to_dict() for livre in self.livres], f, indent=4)

        with open("data/membres.json", "w", encoding="utf-8") as f:
            json.dump([membre.to_dict() for membre in self.membres], f, indent=4)

    def charger(self):
        try:
            with open("data/livres.json", "r", encoding="utf-8") as f:
                self.livres = [Livre.from_dict(d) for d in json.load(f)]
        except FileNotFoundError:
            self.livres = []

        try:
            with open("data/membres.json", "r", encoding="utf-8") as f:
                self.membres = [Membre.from_dict(d, self.livres) for d in json.load(f)]
        except FileNotFoundError:
            self.membres = []

# Ecrire les actions (emprunts ou retours) dans le fichier historique.csv
def enregistrer_action(id_membre, isbn, action="emprunt", fichier="data/historique.csv"):
    # Vérifier si le fichier existe:
    file_exists = os.path.isfile(fichier)
    write_header = False

    if not file_exists:
        write_header = True
    else:
        # Vérifier si le fichier est vide:
        if os.path.getsize(fichier) == 0:
            write_header = True

    with open(fichier, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["date", "isbn", "id_membre", "action"])
        # Ecrire l'en-tête si le fichier est vide:
        if write_header:
            writer.writeheader()
        writer.writerow({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "isbn": isbn,
            "id_membre": id_membre,
            "action": action
        })
