import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'beer_tracker'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:MongoAtlas20@myfirstcluster.zecjr.mongodb.net/beer_tracker?retryWrites=true&w=majority')

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
    ratings=mongo.db.ratings
    ratings.insert_one(request.form.to_dict())
    return redirect(url_for('add_beer'))
    

@app.route('/edit_beer/<beer_id>')
def edit_beer(beer_id):
    the_beer = mongo.db.ratings.find_one({"_id": ObjectId(beer_id)})
    all_ratings = mongo.db.ratings.find()
    return render_template('editbeer.html', beer = the_beer, ratings = all_ratings)
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
