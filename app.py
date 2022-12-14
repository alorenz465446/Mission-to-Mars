# flask app (look at lesson 10.5.1)

# import dependecies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# set up app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# homepage route
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# scrape route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

# close
if __name__ == "__main__":
    app.run()
