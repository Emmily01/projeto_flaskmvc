from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///achados_perdidos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    data_registro = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Ativo') 

    def __repr__(self):
        return f'<Item {self.id} - {self.descricao}>'

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    total_ativos = Item.query.filter_by(status='Ativo').count()
    return render_template('index.html', total=total_ativos)

@app.route('/itens')
def listar_itens():
    itens = Item.query.order_by(Item.data_registro.desc()).all()
    return render_template('itens.html', itens=itens)

@app.route('/itens/novo', methods=['GET', 'POST'])
def novo_item():

        descricao = request.form['descricao']
        categoria = request.form['categoria']
        local = request.form['local']

        novo = Item(descricao=descricao, categoria=categoria, local=local)
        db.session.add(novo)
        db.session.commit()

        return redirect(url_for('listar_itens'))
    
    return render_template('novo_item.html')

@app.route('/itens/<int:id>/devolver', methods=['POST'])
def devolver_item(id):
    item = Item.query.get_or_404(id)
    item.status = 'Devolvido'
    db.session.commit()
    
    return redirect(url_for('listar_itens'))

if __name__ == '__main__':
    app.run(debug=True)