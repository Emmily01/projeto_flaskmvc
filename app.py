from flask import Flask, render_template
from extensions import db, login_manager
from models import User

# Importando os Blueprints
from routes.auth import auth_bp
from routes.itens import itens_bp

app = Flask(__name__)

# Configuração do Banco de Dados
# Certifique-se de que o XAMPP esteja rodando o MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/central_achados'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chave_super_secreta_projeto'

# Inicializando Extensões
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login' 
login_manager.login_message = "Por favor, faça login para acessar essa página."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registrando rotas
app.register_blueprint(auth_bp)
app.register_blueprint(itens_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas automaticamente se não existirem
    app.run(debug=True)