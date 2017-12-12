from flask import Flask, request, jsonify, Response
import json
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)


def getMysqlConnection():
    return mysql.connector.connect(user='thomas', host='mysql', port='3306', password='babar', database='test')


@app.route("/")
def hello():
    return "Salut !"


@app.route('/api/getUsers', methods=['GET'])
@cross_origin()  # allow all origins all methods.
def get_users():
    db = getMysqlConnection()
    print(db)
    sqlstr = "SELECT * from user"
    print(sqlstr)
    cur = db.cursor()
    cur.execute(sqlstr)
    return jsonify(data=cur.fetchall())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
