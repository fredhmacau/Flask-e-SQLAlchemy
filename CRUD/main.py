
from flask import Flask, render_template, url_for, request

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder='static', template_folder='templates')
# mysql='mysql://root:@localhost:3306/flask_crud'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///store.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Tabela de Usuarios


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(90), nullable=False)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        hash_pw = generate_password_hash(
            request.form['senha'], method='sha256')
        new_user = User(username=request.form['nome'], password=hash_pw)
        db.session.add(new_user)
        db.session.commit()
        msg = True
        return render_template('cadastro.html', msg=msg)

    return render_template("cadastro.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = User.query.filter_by(username=request.form['nome']).first()
        if login and check_password_hash(login.password, request.form['senha']):
            msg_status = True
            return render_template('login.html', status=msg_status)
        else:
            msg_status = False
            return render_template('login.html', status=msg_status)

    return render_template('login.html')



@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method=='GET':
        search=request.args.get('search')
        research=User.query.filter(User.username.endswith(search)).all()
        status_search=False
        if research:
            status_search=True
            research.username
           
        
    return render_template('index.html',status_search=status_search,user=research)






if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'secret'
    db.create_all()
    app.run(debug=True)
