from flask import Flask, render_template
from extensions import db, login_manager
from models import User
from routes.auth import auth_bp
from routes.itens import itens_bp

app = Flask(__name__)

import os

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'achados_perdidos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chave_super_secreta_projeto'

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login' 
login_manager.login_message = "Por favor, faça login para acessar essa página."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp)
app.register_blueprint(itens_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)