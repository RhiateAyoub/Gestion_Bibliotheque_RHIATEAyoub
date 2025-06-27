import matplotlib.pyplot as plt
from collections import Counter
import csv
from datetime import datetime, timedelta
import os

# Si le dossier n'existe pas, créer le:
os.makedirs("assets", exist_ok=True)

# --------------------- Répartition des livres par genre ---------------------
def diagramme_genres(livres):
    # Retrouver les genres
    genres = [livre.genre for livre in livres]
    genre_count = Counter(genres)

    plt.figure(figsize=(6, 6))
    plt.pie(genre_count.values(), labels=genre_count.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Répartition des livres par genre")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig("assets/stats_genres.png")
    plt.show()


# --------------------- Top N des auteurs les plus populaires ---------------------
def top_auteurs(livres, top_n=10):
    # Retrouver les auteurs
    auteurs = [livre.auteur for livre in livres]
    auteur_count = Counter(auteurs).most_common(top_n)

    noms = [a[0] for a in auteur_count]
    nb_livres = [a[1] for a in auteur_count]

    plt.figure(figsize=(10, 5))
    plt.bar(noms, nb_livres, color='darkorange')
    plt.title(f"Top {top_n} des auteurs les plus populaires")
    plt.xlabel("Auteur")
    plt.ylabel("Nombre de livres")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("assets/stats_auteurs.png")
    plt.show()


# --------------------- Activité des emprunts (30 derniers jours) ---------------------
def activite_emprunts(fichier_csv):
    dates = []

    with open(fichier_csv, newline='', encoding='utf-8') as f:
        lecteur = csv.DictReader(f)
        # Retrouver les dates des emprunts
        for ligne in lecteur:
            if "action" not in ligne or "date" not in ligne:
                continue  # Protection basique
            if ligne["action"].strip().lower() == "emprunt":
                try:
                    date = datetime.strptime(ligne["date"].strip(), "%Y-%m-%d").date()
                    dates.append(date)
                except ValueError:
                    continue

    aujourd_hui = datetime.now().date()
    il_y_a_30_jours = aujourd_hui - timedelta(days=30)
    dates_recents = [d for d in dates if il_y_a_30_jours <= d <= aujourd_hui]

    activite = Counter(dates_recents)
    jours = [il_y_a_30_jours + timedelta(days=i) for i in range(31)]
    emprunts_par_jour = [activite.get(jour, 0) for jour in jours]

    plt.figure(figsize=(12, 5))
    plt.plot(jours, emprunts_par_jour, marker='o')
    plt.title("Activité des emprunts (30 derniers jours)")
    plt.xlabel("Date")
    plt.ylabel("Nombre d'emprunts")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("assets/stats_emprunts.png")
    plt.show()
