from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models import Item
from datetime import datetime

itens_bp = Blueprint('itens', __name__)

@itens_bp.route('/itens')
def listar_itens():
    itens = Item.query.order_by(Item.data_registro.desc()).all()
    return render_template('itens.html', itens=itens)

@itens_bp.route('/itens/novo', methods=['GET', 'POST'])
@login_required 
def novo_item():
    if request.method == 'POST':
        descricao = request.form['descricao']
        categoria = request.form['categoria']
        local = request.form['local']
        
        novo_item = Item(
            descricao=descricao,
            categoria=categoria,
            local_encontrado=local,
            status='Ativo'
        )
        
        db.session.add(novo_item)
        db.session.commit()
        flash('Item registrado com sucesso!', 'success')
        return redirect(url_for('itens.listar_itens'))
    
    return render_template('novo_item.html')

@itens_bp.route('/itens/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_item(id):
    item = Item.query.get_or_404(id)
    
    if request.method == 'POST':
        item.descricao = request.form['descricao']
        item.categoria = request.form['categoria']
        item.local_encontrado = request.form['local']
        
        db.session.commit()
        flash('Item atualizado com sucesso.', 'success')
        return redirect(url_for('itens.listar_itens'))
        
    return render_template('editar_item.html', item=item)

@itens_bp.route('/itens/<int:id>/remover', methods=['POST'])
@login_required
def remover_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Item removido.', 'success')
    return redirect(url_for('itens.listar_itens'))

# Rota para "Pedir/Emprestar" o item
@itens_bp.route('/itens/<int:id>/devolver', methods=['POST'])
@login_required
def devolver_item(id):
    item = Item.query.get_or_404(id)
    nome_quem_pegou = request.form['nome_retirada']
    
    item.status = 'Emprestado'
    item.retirado_por = nome_quem_pegou
    item.data_devolucao = datetime.now()
    
    db.session.commit()
    flash(f'Item marcado como emprestado para {nome_quem_pegou}.', 'info')
    return redirect(url_for('itens.listar_itens'))