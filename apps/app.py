from flask import jsonify
from flask_classful import FlaskView
from flask import Flask, jsonify
from models import Person, Pet, Food, db, app
import secrets

res = [
    "hello world"
]


class PersonView(FlaskView):
    """
    Description of PersonView

    Inheritance:
        FlaskView:

    """
    
    # create person
    def create(self):
   
        person = Person(name="Bani2", country="Brasil")
        db.session.add(person)
        db.session.commit()
        results = [{"name": person.name}
                   for person in Person.query.filter_by(id=person.id)]
        return jsonify(results=results)

    # Nombrar los nombres de todas sus mascotas
    
    def get_all_pets_names(self):
        """
        Description of get_all_pets_names

        Args:
            self (undefined):

        """
        persons = Pet.query.all()
        results = [{"name": person.name} for person in persons]
        return jsonify(results=results)

    # Dar comida a una mascota (La mascota solo aceptará la comida que le gusta, no se acepta comida)
    def give_food_for_an_pet(self):
        return secrets.SystemRandom().choice(res)

    # Preparar comida
    def cook_the_food(self):
        return secrets.SystemRandom().choice(res)

    # Obtener una nueva mascota
    def get_a_new_pet(self):
        person = Person(name="Bani", country="Brasil")
        db.session.add(person)
        db.session.commit()
        return secrets.SystemRandom().choice(res)

    '''
    5:# Revisar si la comida se ha podrido (verificar fecha de caducidad y podrir la comida si se paso)
    
    6:# Comer (Aumenta su salud) 
    
    7:# Dormir (Aumenta su estado de sueño) 
    
    8:# Revisar mascotas (Si la mascota tiene salud <=0 debe morir)
    
    9:# Presentarse (Mostrar su información) 
    '''


PersonView.register(app, route_base='/person')


class PetView(FlaskView):
    """
    Description of PetView

    Inheritance:
        FlaskView:

    """
    
    def eat_food(self):  # Comer comida (Si come comida podrida, se le restara 40 de salud, sino aumentar 70 de salud)
        return secrets.SystemRandom().choice(res)

    '''
    2:# Saludar a la persona que lo cuida diciendo su comida favorita 

    3:# Comunicarse (Se puede usar un print) 

    3:# Jugar con otra mascota (Las mascotas solo juegan con otras mascotas del mismo tipo)

    4:# Dormir (Aumenta su estado de sueño) 

    5:# Morir  
    '''


PetView.register(app)

    
class FoodView(FlaskView):
    """
    Description of FoodView

    Inheritance:
        FlaskView:

    """
    
    def rotting_food(self):  # Podrirse (La comida se pudre)
        return secrets.SystemRandom().choice(res)

    '''
    2:# Información (Describe quien lo preparó, y que mascotas pueden alimentarse de esta)

    '''


FoodView.register(app)


# db.create_all()
if __name__ == "__main__":
    app.run(debug=True)
