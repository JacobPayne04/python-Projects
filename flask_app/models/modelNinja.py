from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


#TODO change things to ninjas stuff
class Ninja:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends#

        all_ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            all_ninjas.append( cls(ninja) )
        return all_ninjas

    @classmethod
    def add_new_ninja(cls, data):
        query = "INSERT INTO ninjas(first_name,last_name,age,dojo_id) VALUE (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);" #When using %()s, you must pass in data
        new_ninja= connectToMySQL(DATABASE).query_db(query,data) #Returns back an INT, the ID of the row inserted
        return new_ninja

    @classmethod
    def get_ninjas_by_dojo(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.dojo_id=%(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
















