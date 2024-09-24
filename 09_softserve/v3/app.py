# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go? the same results as two?, nowhere
    return "No hablo queso!"

app.debug = True #this is new? maybe it prints more debugging information to the terminal while the server is running
app.run()

#interesting, with debug on it printed the first line and then name, which was main, followed by the server url date and time