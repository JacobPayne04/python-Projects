from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE



#nto sure if i need? coppied from notes 
# class User:
#     @classmethod
#     def get_by_email(cls,data):
#         query = "SELECT * FROM users WHERE email = %(email)s;"
#         result = connectToMySQL("mydb").query_db(query,data)
#         # Didn't find a matching user
#         if len(result) < 1:
#             return False
#         return cls(result[0])