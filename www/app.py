from flask import Flask, request, jsonify, Response
import json
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)


def getMysqlConnection():
    return mysql.connector.connect(user='thomas', host='mysql', port='3306', password='babar', database='test')

def renderWelcome():
    return "<h1>Bienvenue !</h1>" \
    "<p>Cette page web a pour but de montrer le fonctionnement de mon environnement <strong>Docker</strong></p>" \
    "<p>En effet, 2 images ont ete crees pour arriver a ce resultat :</p>" \
           "<ul><li>Une image faisant tourner un serveur python</li>" \
           "<li>Une image faisant tourner un serveur mysql</li></ul>" \
           "<p>Si vous pouvez lire ce texte en ce moment meme, cela signifie que le container python tourne correctement</p>" \
           "<p>Pour tester le lien avec le container MySQL, simulons une fausse API permettant de recuperer des infos de la BDD</p>" \
           "<p>Pour cela, rajoutez <bold><strong>/api/getUsers</strong></bold> a la fin de l'url actuelle !</p>" \
           "<p>Les sources du projets sont entierements disponibles sur mon github : <a href='https://github.com/ThomasEcalle/test-docker'>github</a>"


@app.route("/")
def hello():
    return renderWelcome()


@app.route('/api/getUsers', methods=['GET'])
@cross_origin()  # allow all origins all methods.
def get_users():
    db = getMysqlConnection()
    print(db)
    sqlstr = "SELECT * from user"
    print(sqlstr)
    cur = db.cursor()

    cur.execute(sqlstr)
    data = cur.fetchall()
    db.close()
    return jsonify(data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
