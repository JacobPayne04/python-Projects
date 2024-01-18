# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# model the class after the friend table from our database
class User:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        all_users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            all_users.append( cls(user) )
        return all_users
    
    @classmethod
    def create_new(cls, data:dict):
        query = "INSERT INTO users(first_name,last_name,email) VALUE (%(first_name)s,%(last_name)s,%(email)s)" #When using %()s, you must pass in data
        new_row_id= connectToMySQL(DATABASE).query_db(query,data) #Returns back an INT, the ID of the row inserted
        return new_row_id
    
    @classmethod
    def get_one_by_id(cls, id):
        data = {
            'id':id
        }
        query = """
            SELECT * FROM users
            WHERE id = %(id)s;
        """

        results = connectToMySQL(DATABASE).query_db(query, data)
        # for safety bug catch
        if results:
            row = results[0] # and only result
            return cls(row)

    @classmethod
    def update_users   (cls, data):
        # data = {
        #     'id':id
        # }

        query = """
            UPDATE users
            SET first_name = %(first_name)s,
            last_name  = %(last_name)s,
            email   = %(email)s,

            WHERE id = %(id)s;
        """

        connectToMySQL('users').query_db(query,data )


    @classmethod
    def user_delete(cls, id):

        data = {
            'id':id
        }

        query  = """
            DELETE FROM users 
            WHERE id = %(id)s;
        """

        connectToMySQL(DATABASE).query_db(query, data)
        
