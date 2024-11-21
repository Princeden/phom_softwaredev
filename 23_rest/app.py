import urllib.request
import json
from flask import Flask, render_template

key = open("key_nasa.txt", "r")
api_key = key.read()
key.close()
app = Flask(__name__)
@app.route('/')
def main():
    page = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=" + api_key)
    data = json.loads(page.read())
    return render_template('main.html', explanation = data['explanation'], image = data['hdurl'])

if __name__ == "__main__":
    app.debug = True 
    app.run()
