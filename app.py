from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('film', user='postgres',
                        password='12345', host='localhost', port=5423)


class BaseModel(Model):
    class Meta:
        database = db


class Movie(BaseModel):
    name = CharField()
    year = CharField()
    director = CharField()
    kill_counts = CharField()


db.connect()
db.drop_tables([Movie])
db.create_tables([Movie])

app = Flask(__name__)


@app.route('/movie/', methods=['GET', 'POST'])
@app.route('/movie/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Movie.get(Movie.id == id)))
        else:
            movieList = []
            for movie in Movie.select():
                movieList.append(model_to_dict(movie))
            return jsonify(movieList)

    if request.method == 'POST':
        new_movie = dict_to_model(Movie, request.get_json())
        new_movie.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        return 'DELETE request'


app.run(debug=True, port=5432)
