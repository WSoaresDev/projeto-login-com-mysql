import os
from flask import Flask, render_template, request, redirect, flash, url_for
import pymysql
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)
# Se o .env falhar, ele usa essa chave padrão para não dar erro
app.secret_key = os.getenv('SECRET_KEY', 'chave_segura_123')

def conecta_db():
    # Se DB_PASSWORD for 'SUA_SENHA' no .env e seu banco não tiver senha, vai dar erro.
    # No XAMPP o padrão é usuário 'root' e senha vazia ''.
    senha = os.getenv('DB_PASSWORD')
    if senha == "SUA_SENHA": senha = "" 

    return pymysql.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=senha,
        database=os.getenv('DB_NAME', 'projeto_login'),
        cursorclass=pymysql.cursors.DictCursor
    )

# --- ROTAS DE NAVEGAÇÃO ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tela_cadastro')
def tela_cadastro():
    return render_template('cadastro.html')

# --- LÓGICA DE CADASTRO ---

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha_plana = request.form['senha']
    
    # Gera a senha protegida (Hash)
    senha_criptografada = generate_password_hash(senha_plana)
    
    try:
        db = conecta_db()
        with db.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", 
                           (nome, email, senha_criptografada))
            db.commit()
        db.close()
        flash("Cadastro realizado com sucesso!")
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"Erro ao cadastrar: {e}")
        return redirect(url_for('tela_cadastro'))

# --- LÓGICA DE LOGIN ---

@app.route('/login', methods=['POST'])
def login():
    email = request.form['login']
    senha_digitada = request.form['senha']
    
    db = conecta_db()
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
        usuario = cursor.fetchone()
    db.close()

    # Compara a senha digitada com a criptografada do banco
    if usuario and check_password_hash(usuario['senha'], senha_digitada):
        return f"<h1>Bem-vindo, {usuario['nome']}! Login realizado com segurança.</h1>"
    else:
        flash("Dados incorretos!")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)