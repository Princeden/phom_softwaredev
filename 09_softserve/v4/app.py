# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
#    print("test")
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported 
#if the file is imported what does the name become?
    app.debug = True            # enable auto-reload upon code change
    app.run()
    
#when run it will set debug true and run the flask server, and print "the __name_ of this .." is and name while no hablo queso appears on the page
#the live update actually did happen every time you saved and reloaded the page, and the predictoin was accurate.
    
