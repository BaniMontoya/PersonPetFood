from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/PersonPetFood"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Person(db.Model):
    """
    Description of Person

    Inheritance:
        db.Model:

    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    health = db.Column(db.Integer)
    vitality = db.Column(db.Boolean)

    def __repr__(self):
        """
        Description of __repr__

        Args:
            self (undefined):

        """
        return f"<Person> {self.name}"


class Pet(db.Model):
    """
    Description of Pet

    Inheritance:
        db.Model:

    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    health = db.Column(db.Integer)
    vitality = db.Column(db.Boolean)

    person_id = db.Column('person_id', db.Integer, db.ForeignKey('person.id'))
    person = db.relationship('Person', foreign_keys=person_id)

    def __repr__(self):
        """
        Description of __repr__

        Args:
            self (undefined):

        """
        return f"<Pet> {self.name}"


class Food(db.Model):
    """
    Description of Food

    Inheritance:
        db.Model:

    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    health = db.Column(db.Integer)
    person_id = db.Column('person_id', db.Integer, db.ForeignKey('person.id'))
    person = db.relationship('Person', foreign_keys=person_id)
    pet_id = db.Column('pet_id', db.Integer, db.ForeignKey('pet.id'))
    pet = db.relationship('Pet', foreign_keys=pet_id)
    vitality = db.Column(db.Boolean)

    def __repr__(self):
        """
        Description of __repr__

        Args:
            self (undefined):

        """
        return f"<Food> {self.name}"
