import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path

if path.exists('env.py'):
    import env


MONGO_URI = os.environ.get('MONGO_URI')

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'beer_tracker'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_beer')
def get_beer():
    return render_template("beers.html", ratings=mongo.db.ratings.find())


@app.route('/add_beer')
def add_beer():
    return render_template("addbeer.html", ratings=mongo.db.ratings.find())


@app.route('/insert_beer', methods=['POST'])
def insert_beer():
    ratings = mongo.db.ratings
    ratings.insert_one(request.form.to_dict())
    return redirect(url_for('get_beer'))


@app.route('/edit_beer/<beer_id>')
def edit_beer(beer_id):
    the_beer = mongo.db.ratings.find_one({"_id": ObjectId(beer_id)})
    all_ratings = mongo.db.ratings.find()
    return render_template('editbeer.html', beer=the_beer, ratings=all_ratings)


@app.route('/update_beer/<beer_id>', methods=['POST'])
def update_beer(beer_id):
    ratings = mongo.db.ratings
    ratings.update({'_id': ObjectId(beer_id)},
        {
            'beer_name': request.form.get('beer_name'),
            'brewery_name': request.form.get('brewery_name'),
            'beer_location': request.form.get('beer_location'),
            'drank_date': request.form.get('drank_date'),
            'beer_comm': request.form.get('beer_comm'),
            'beer_rating': request.form.get('beer_rating'),
            'soc_dist': request.form.get('soc_dist'),
        })
    return redirect(url_for('get_beer'))


@app.route('/delete_beer/<beer_id>')
def delete_beer(beer_id):
    print('delete route accessed')
    mongo.db.ratings.remove({'_id': ObjectId(beer_id)})
    return redirect(url_for('get_beer'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
