# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024
#no print function, should still work fine and create a page with no hablo queso
#prediction was correct
from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

