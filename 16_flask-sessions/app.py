#to do reminder: change authenticate to process both get and post
from flask import Flask, request, render_template, session

app = Flask(__name__)
app.secret_key ='secret'
@app.route("/" , methods=['GET', 'POST'])
def disp_login():
    if 'username' in session:
        return render_template('home.html', username = session['username'])
    else:
        return render_template( 'login.html' )

@app.route("/auth" , methods=['GET', 'POST'])
def authenticate():
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
    #print("***DIAG: request obj ***")
    #print(request)
    #print("***DIAG: request.args ***")
    #print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    #print("***DIAG: request.headers ***")
    #print(request.headers)
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('home.html', username = username)  #response to a form submission
@app.route('/logout')
def logout():
    session.pop('username')
    return render_template('login.html')
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
