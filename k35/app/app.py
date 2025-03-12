from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('stories', lazy=True))
    contributions = db.relationship('Contribution', backref='story', lazy=True)

class Contribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False)
    contributor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contributor = db.relationship('User', backref=db.backref('contributions', lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    stories = Story.query.all()
    return render_template('home.html', stories=stories)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/add_story', methods=['GET', 'POST'])
@login_required
def add_story():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_story = Story(title=title, content=content, author_id=current_user.id)
        db.session.add(new_story)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_story.html')

@app.route('/edit_story/<int:story_id>', methods=['GET', 'POST'])
@login_required
def edit_story(story_id):
    story = Story.query.get_or_404(story_id)

    # Check if the user is the original author of the story
    if story.author_id == current_user.id:
        flash("You cannot edit your own story.", "danger")
        return redirect(url_for('home'))

    # Check if the user has already contributed to this story
    existing_contribution = Contribution.query.filter_by(story_id=story_id, contributor_id=current_user.id).first()
    if existing_contribution:
        flash("You have already contributed to this story.", "danger")
        return redirect(url_for('home'))

    if request.method == 'POST':
        content = request.form['content']
        new_contribution = Contribution(content=content, story_id=story_id, contributor_id=current_user.id)
        db.session.add(new_contribution)
        db.session.commit()
        flash("Your contribution has been added.", "success")
        return redirect(url_for('home'))

    return render_template('edit_story.html', story=story)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
