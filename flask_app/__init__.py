from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Keep it safe"
DATABASE = "dojos_and_ninjas_schema"