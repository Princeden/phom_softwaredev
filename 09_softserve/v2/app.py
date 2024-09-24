# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go? probably on the page created along with about to print
    return "No hablo queso!"      #prediction was wrong, the message before print(__name__) did not appear, only the message after
                                  #did not print anywhere
app.run()
