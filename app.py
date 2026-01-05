from flask import Flask, render_template, request, redirect, flash, url_for
import pymysql

app = Flask(__name__)
app.secret_key = 'projeto_vidro_123'

# Configuração do Banco
def conecta_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='9688', # Se tiver senha no seu MySQL, coloque aqui
        database='projeto_login',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tela_cadastro')
def tela_cadastro():
    return render_template('cadastro.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['login']
    senha = request.form['senha']
    
    db = conecta_db()
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios WHERE email=%s AND senha=%s", (email, senha))
        usuario = cursor.fetchone()
    db.close()
    
    if usuario:
        return f"<h1>Bem-vindo, {usuario['nome']}! Login realizado.</h1>"
    else:
        flash("Senha ou Usuário incorretos!")
        return redirect(url_for('index'))

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    
    try:
        db = conecta_db()
        with db.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
            db.commit()
        db.close()
        flash("Cadastro realizado com sucesso! Faça seu login.")
        return redirect(url_for('index'))
    except:
        flash("Erro: Este e-mail já está cadastrado.")
        return redirect(url_for('tela_cadastro'))

if __name__ == '__main__':
    app.run(debug=True)