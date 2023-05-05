# -------------------- MODULES -------------------- #
# imported Flask, jsonify, render_template, and request class from flask module
from flask import Flask, jsonify, render_template, request

# imported SQLAlchemy class
from flask_sqlalchemy import SQLAlchemy


# -------------------- APP -------------------- #
# instantiating Flask class and storing it in a variable called app
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# -------------------- TABLE -------------------- #
##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


# -------------------- ROUTES -------------------- #
# route decorator to tell flask run this function when someone access the home page
@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


# -------------------- MAIN -------------------- #
# checks if name is equal to main and if it is, it will run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
