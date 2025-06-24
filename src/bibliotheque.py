import json
from exceptions import *

class Livre:
    def __init__(self, isbn, titre, auteur, annee, genre):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
        else:
            raise LivreIndisponibleError()

    def rendre(self):
        if not self.disponible:
            self.disponible = True
        else:
            raise LivreIndisponibleError("Le livre n'est pas emprunté.")

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titre": self.titre,
            "auteur": self.auteur,
            "annee": self.annee,
            "genre": self.genre,
            "disponible": self.disponible
        }

    def from_dict(self, data):
        return Livre(
            isbn = data["isbn"],
            titre = data["titre"],
            auteur = data["auteur"],
            annee = data["annee"],
            genre = data["genre"]
        )

class Membre:
    def __init__(self, id_membre, nom):
        self.id_membre = id_membre
        self.nom = nom
        self.livres_empruntes = []

    def emprunter_livre(self, livre:Livre):
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
            self.livres_empruntes.remove(livre)
        else:
            raise LivreIndisponibleError("Le livre n'est pas emprunté.")

    def to_dict(self):
        return {
            "id_membre": self.id_membre,
            "nom": self.nom,
            "livres_empruntes": [livre.to_dict() for livre in self.livres_empruntes]
        }

    def from_dict(self, data):
        membre = Membre(data["id_membre"], data["nom"])
        membre.livres_empruntes = [Livre.from_dict(livre_data) for livre_data in data.get("livres_empruntes", [])]
        return membre
            

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.membres= []

    def ajouter_livre(self, livre:Livre):
        self.livres.append(livre)

    def ajouter_membre(self, membre:Membre):
        self.membres.append(membre)
        
    def emprunter_livre(self, id_membre, titre_livre):
        mbr = None
        lvr = None
        for membre in self.membres:
            if membre.id_membre == id_membre:
                mbr = membre
                break
        if mbr is None:
            raise MembreInexistantError()
        for livre in self.livres:
            if livre.titre == titre_livre:
                lvr = livre
                break
        if lvr is None:
            raise LivreInexistantError()
        mbr.emprunter_livre(lvr)

    def rendre_livre(self, id_membre, titre_livre):
        mbr = None
        lvr = None
        for membre in self.membres:
            if membre.id_membre == id_membre:
                mbr = membre
                break
        if mbr is None:
            raise MembreInexistantError()
        for livre in mbr.livres_empruntes:
            if livre.titre == titre_livre:
                lvr = livre
                break
        if lvr is None:
            raise LivreInexistantError("Ce membre n'a pas emprunté ce livre!")
        mbr.rendre_livre(lvr)

    def sauvegarder(self):
        with open("../data/livres.json", "w", encoding="utf-8") as f:
            json.dump([livre.to_dict() for livre in self.livres], f, indent=4)

        with open("../data/membres.json", "w", encoding="utf-8") as f:
            json.dump([membre.to_dict() for membre in self.membres], f, indent=4)

    def charger(self):
        try:
            with open("../data/livres.json", "r", encoding="utf-8") as f:
                self.livres = [Livre.from_dict(d) for d in json.load(f)]
        except FileNotFoundError:
            self.livres = []

        try:
            with open("../data/membres.json", "r", encoding="utf-8") as f:
                self.membres = [Membre.from_dict(d) for d in json.load(f)]
        except FileNotFoundError:
            self.membres = []
