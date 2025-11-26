from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///achados_perdidos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'uma-senha-secreta-bem-dificil' 

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' 

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    data_registro = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Ativo')
    retirado_por = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Item {self.id} - {self.descricao}>'
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('listar_itens'))
        else:
            flash('Login inválido. Verifique usuário e senha.')
            
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password, method='scrypt')
        
        novo_usuario = User(username=username, password=hashed_password)
        
        try:
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Conta criada com sucesso! Faça login.')
            return redirect(url_for('login'))
        except:
            flash('Esse usuário já existe.')
            
    return render_template('registro.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
def index():
    total_ativos = Item.query.filter_by(status='Ativo').count()
    return render_template('index.html', total=total_ativos)

@app.route('/itens')
def listar_itens():
    itens = Item.query.order_by(Item.data_registro.desc()).all()
    return render_template('itens.html', itens=itens)

@app.route('/itens/novo', methods=['GET', 'POST'])
@login_required 
def novo_item():
    if request.method == 'POST':
        descricao = request.form['descricao']
        categoria = request.form['categoria']
        local = request.form['local']

        novo = Item(descricao=descricao, categoria=categoria, local=local)
        db.session.add(novo)
        db.session.commit()

        return redirect(url_for('listar_itens'))
    
    return render_template('novo_item.html')

@app.route('/itens/<int:id>/devolver', methods=['POST'])
@login_required 
def devolver_item(id):
    item = Item.query.get_or_404(id)
    
    nome_retirada = request.form['nome_retirada']
    
    item.status = 'Devolvido'
    item.retirado_por = nome_retirada 
    
    db.session.commit()
    
    return redirect(url_for('listar_itens'))

if __name__ == '__main__':
    app.run(debug=True)
