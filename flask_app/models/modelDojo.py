from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Dojo:
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated = data['updated_at']

    @classmethod
    def get_all_dojo_m(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends#
    
        all_dojos = []
        each_dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            all_dojos.append( cls(dojo) )
        return all_dojos
    #retunr intances #TODO

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUE (%(name)s);"#change this
        # make sure to call the connectToMySQL function with the schema you are targeting.
        new_added_dojo = connectToMySQL(DATABASE).query_db(query, data)
        return new_added_dojo
        

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id=%(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
