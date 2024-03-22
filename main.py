
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marathi_lessons.db'
db = SQLAlchemy(app)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    lessons = Lesson.query.all()
    return render_template('lessons.html', lessons=lessons)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
