## 📚 Gestion Bibliothèque
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-En%20cours-yellow)
![Interface](https://img.shields.io/badge/interface-CLI-orange)

Une application en ligne de commande (CLI), développée en **Python**, pour gérer les livres, les membres, les emprunts et les rendus d'une bibliothèque.
Le projet inclut également des visualisations graphiques avec `matplotlib` pour l’analyse des données 📊

---

## 👨‍💻 Auteur

Ayoub Rhiate.

Développé dans le cadre d’un mini-projet universitaire en génie informatique 🧠💻

---

### 🛠️ Fonctionnalités

* Ajouter et lister des livres
* Inscrire des membres
* Emprunter et rendre des livres
* Sauvegarde et persistance des données (`.json` / `.csv`)
* Visualisations :

  * Diagramme circulaire des genres de livres
  * Auteurs les plus populaires
  * Courbe des emprunts des 30 derniers jours

---

## 🚀 Installation

### ✅ Prérequis

* Python 3.10 ou plus recommandé
* `pip` (gestionnaire de paquets)

1. **Cloner le dépôt**

```bash
git clone https://github.com/RhiateAyoub/Gestion_Bibliotheque_RHIATEAyoub
cd CheminVers/gestion-bibliotheque
```
2. **📦 Installer les dépendances**

```bash
pip install -r requirements.txt
```

> 📁 Les fichiers de données sont stockés dans le dossier `data/` :
>
> * `livres.json` — livres enregistrés
> * `membres.json` — membres inscrits
> * `historique.csv` — historique des emprunts/retours

---

## ▶️ Exécution

Dans le terminal, lancez :

```bash
python src/main.py
```

Vous verrez un menu interactif :

```
=== GESTION BIBLIOTHEQUE ===
  1. Ajouter un livre
  2. Inscrire un membre
  3. Emprunter un livre
  4. Rendre un livre
  5. Lister tous les livres
  6. Lister tous les membres
  7. Afficher les statistiques
  8. Sauvegarder et quitter
```

---

## 💡 Exemples d'utilisation

### ➕ Ajouter un livre :

```
Titre: Le Petit Prince
Auteur: Antoine de Saint-Exupéry
ISBN: 9782070612758
Année: 1943
Genre: Conte philosophique
```

### 👤 Inscrire un membre :

```
ID membre: 101
Nom: Alice Dupont
```

### 📕 Emprunter un livre :

```
ID membre: 101
Titre: Le Petit Prince
```

### 📈 Visualiser les statistiques :

* Répartition des genres (camembert)
* Top auteurs les plus fréquents
* Activité des emprunts (30 jours)

---

## 📁 Arborescence

```
Gestion_Bibliotheque/
│
├── data/
│   ├── livres.json
│   ├── membres.json
│   └── historique.csv
│
├── src/
│   ├── main.py
│   ├── bibliotheque.py
│   ├── exceptions.py
│   └── visualisations.py
│
├── assets/
│   ├── stats_genres.png
│   ├── stats_auteurs.png
│   ├── stats_emprunts.png
│   └── presentation.mp4
│
├── docs/
│   └── rapport.pdf
│
├── requirements.txt
└── README.md
```
