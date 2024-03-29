from flask import Flask  # Import Flask to allow us to create our app
from flask_bcrypt import Bcrypt
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Keep it safe"

bcrypt = Bcrypt(app)

DATABASE = "users_schema_db"