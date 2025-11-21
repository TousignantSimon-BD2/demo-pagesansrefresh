import os
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    """Cette fonction-là, elle fait juste se connecter à la base de données MySQL."""
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        return conn
    except Error as e:
        print(f"Oups, erreur de connexion à la base de données: {e}")
        return None

@app.route('/')
def index():
    """Quand quelqu'un arrive sur la page d'accueil, on lui sert le fichier index.html."""
    return render_template('index.html')

@app.route('/api/voiture/<int:id>')
def get_voiture(id):
    """
    Ça, c'est la page spéciale que le javascript va appeler.
    Elle retourne les infos d'une voiture en format JSON. La page web va comprendre ça
    pis s'en servir pour remplir les champs.
    """
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Erreur de connexion à la base de données'}), 500
        
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, marque, modele FROM voiture WHERE id = %s", (id,))
        voiture = cursor.fetchone()
        
        if voiture:
            return jsonify(voiture)
        else:
            return jsonify({'error': 'Voiture non trouvée'}), 404
    except Error as e:
        print(f"Oups, erreur avec la requête SQL: {e}")
        return jsonify({'error': 'Erreur interne du serveur'}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
