import os
from flask import Flask
from flask import Response
from flask import jsonify
import psycopg2

flask_app = Flask(__name__)
flask_port = int(os.getenv("VCAP_APP_PORT", 88))

# I wouldn't hardcode connection credentials in anything - only for this exercise
db = psycopg2.connect(host="db-service", database="oreilly", user="oreilly", password="hunter2")
db_cursor = db.cursor()


@flask_app.route('/')
def index():
    db_cursor.execute("SELECT * FROM works")
    return jsonify(get_dict(db_cursor))
        

@flask_app.route('/works/<work_id>')
def get_work_by_id(work_id):
    db_cursor.execute("SELECT * FROM works WHERE work_id = {}".format(work_id))
    return jsonify(get_dict(db_cursor))


@flask_app.route('/isbn/<isbn>')
def get_work_by_isbn(isbn):
    db_cursor.execute("SELECT * FROM works WHERE isbn LIKE '{}'".format(isbn))
    return jsonify(get_dict(db_cursor))


@flask_app.route('/titles/<title>')
def get_works_by_title(title):
    db_cursor.execute("SELECT * FROM works WHERE title ILIKE '%{}%'".format(title))
    return jsonify(get_dict(db_cursor))


@flask_app.route('/authors/<author>')
def get_works_by_author(author):
    db_cursor.execute("SELECT * FROM works WHERE authors ILIKE '%{}%'".format(author))
    return jsonify(get_dict(db_cursor))


def get_dict(cursor):
    works = []
    column_names = []
    for col in cursor.description:
        column_names.append(col[0])

    records = cursor.fetchall()
    for row in records:
        work = {}
        for i in range(len(column_names)):
            work[column_names[i]] = str(row[i])
        works.append(work)
            
    return works


if __name__ == '__main__':
    flask_app.run(host = '0.0.0.0', port = flask_port)