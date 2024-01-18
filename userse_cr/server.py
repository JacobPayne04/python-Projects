from flask_app import app
#For every controller file, add below 
from flask_app.controllers import controller


#This is always at the bottom!
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
