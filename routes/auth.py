from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from extensions import db
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
                user = User.query.filter_by(username=username).first()
        
        if not user:
            flash('Usuário não encontrado. Por favor, faça seu cadastro primeiro.', 'warning')
            return redirect(url_for('auth.registro'))
        if not check_password_hash(user.password, password):
            flash('Senha incorreta. Tente novamente.', 'danger')
            return redirect(url_for('auth.login'))
            
        login_user(user)
        flash(f'Bem-vindo de volta, {user.username}!', 'success')
        return redirect(url_for('index')) 
            
    return render_template('login.html')

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
                user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('Erro: Esse nome de usuário já está em uso.', 'danger')
            return redirect(url_for('auth.registro'))

        hashed_password = generate_password_hash(password)
        novo_user = User(username=username, password=hashed_password)
        
        try:
            db.session.add(novo_user)
            db.session.commit()
            flash('Conta criada com sucesso! Agora faça seu login.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash('Erro ao criar conta. Tente novamente.', 'danger')
            
    return render_template('registro.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('index'))