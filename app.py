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
    return render_template("addbeer.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
