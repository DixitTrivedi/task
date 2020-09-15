from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/quizdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    c_name = db.Column(db.String(100))
    color_name = db.Column(db.String(100))

    def __init__(self, name, c_name, color_name):
        self.name = name
        self.c_name = c_name
        self.color_name = str(color_name)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == "POST":
        name = request.form.get('name_id')
        c_name = request.form.get('c_name')
        color_name = request.form.getlist('color_name')

        myData = Data(name, c_name, color_name)
        db.session.add(myData)
        db.session.commit()
        return render_template('index.html', name=name, c_name=c_name, color_name=color_name)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)