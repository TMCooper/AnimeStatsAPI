# AnimeStats API

AnimeStats est une solution légère d'analyse et de visualisation de données de consommation d'anime. Elle se compose d'une API REST Flask pour collecter les statistiques de visionnage et d'un tableau de bord interactif pour explorer les données (tendances, genres, studios, activité temporelle).

Le projet enrichit les données locales avec des métadonnées externes via l'API Jikan (MyAnimeList).

## 📋 Fonctionnalités

*   **Collecte de données** : Endpoint simple pour enregistrer l'anime, la saison et l'épisode visionné.
*   **Stockage Persistant** : Utilisation de SQLite pour une base de données locale légère et rapide.
*   **Dashboard Analytique** : Interface web moderne (TailwindCSS + Chart.js) proposant :
    *   Statistiques globales (temps passé, nombre d'épisodes).
    *   Graphiques d'activité (horaire, quotidienne, annuelle).
    *   Répartition par genres et studios.
    *   Classements (Top téléchargements/visionnages, Top notes).
*   **Enrichissement de métadonnées** : Récupération automatique des pochettes, notes et informations de production via l'API Jikan.
*   **Sécurité** : Protection de l'accès aux données par token administrateur.

## 🛠 Prérequis

*   Python 3.8 ou supérieur
*   Pip (Gestionnaire de paquets Python)

## 🚀 Installation

1.  **Cloner le dépôt**
    ```bash
    git clone https://github.com/votre-username/animestats.git
    cd animestats
    ```

2.  **Créer un environnement virtuel (recommandé)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/MacOS
    source venv/bin/activate
    ```

3.  **Installer les dépendances**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration**
    Créez un fichier `.env` à la racine du projet et définissez votre mot de passe administrateur :
    ```env
    ADMIN_PASSWORD=VotreMotDePasseSecurise
    ```

## ▶️ Démarrage

Lancez l'application via le point d'entrée principal :

```bash
python main.py