# Démo : Aller chercher des infos dans une base de données avec Flask et JavaScript

Salut ! Ce petit projet sert à vous montrer comment on peut aller chercher des informations dans une base de données et les afficher sur une page web sans que la page ait besoin de se recharger au complet.

## Le but du jeu

L'idée, c'est simple :
1.  L'utilisateur entre un ID dans une boîte sur la page web.
2.  Il pèse sur "Rechercher" (ou sur "Enter").
3.  Le JavaScript va chercher les informations de la voiture qui correspond à cet ID.
4.  Les champs vides (marque et modèle) se remplissent tout seuls avec les bonnes informations.

Cette technique, où le JavaScript va chercher des données en arrière-plan, s'appelle **AJAX**. C'est super pratique pour rendre les pages web plus rapides et agréables à utiliser.

## Comment ça marche en dessous du capot ?

Le JavaScript ne va pas voir la base de données directement. À la place, il appelle une page web spéciale qu'on a créée dans notre application Flask (`/api/voiture/<id>`).

Cette page spéciale, c'est pas une page HTML normale. Elle retourne juste un fichier **JSON** (un format de texte ben simple que le JavaScript comprend tout de suite) avec les informations de la voiture.

Flask rend ça super facile avec la fonction `jsonify`. Pas besoin de se casser la tête, tu lui donnes un dictionnaire Python et `jsonify` s'occupe de le transformer en JSON pour que le navigateur soit content.

## Instructions pour les étudiants

Vous pouvez reprendre ce code, le modifier, vous en inspirer pour vos propres projets. Pas besoin de nous citer, c'est fait pour vous aider à apprendre.

## Comment faire rouler le projet

Assurez-vous d'avoir Python et MySQL d'installés sur votre machine.

1.  **Créez un environnement virtuel**
    C'est une bonne habitude pour pas mélanger les dépendances de vos projets.
    ```bash
    python3 -m venv venv
    ```

2.  **Activez l'environnement**
    *   Sur macOS/Linux : `source venv/bin/activate`
    *   Sur Windows (cmd) : `venv\Scripts\activate.bat`

3.  **Installez les paquets nécessaires**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Créez la base de données**
    Le fichier `init.sql` est là pour ça. Il va créer la base de données, la table, pis insérer quelques voitures pour que vous puissiez faire des tests.
    
    **ATTENTION :** Ouvrez le fichier `.env` et assurez-vous que le mot de passe (`DB_PASSWORD`) correspond à celui de votre installation MySQL. J'ai mis `qwerty` comme exemple. Si le vôtre est différent, changez-le dans le fichier `.env` avant de rouler la commande suivante.
    
    ```bash
    # Ça va vous demander le mot de passe que vous avez mis dans le .env
    mysql -u root -p < init.sql
    ```

5.  **Lancez l'application**
    ```bash
    python app.py
    ```

6.  **Testez !**
    Ouvrez votre navigateur web à l'adresse `http://127.0.0.1:5000/`. Vous pouvez tester avec les IDs `1`, `2` ou `3`.
