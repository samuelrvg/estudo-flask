from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'cursoflask'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('GTA', 'Ação', 'PC')
jogo2 = Jogo('Grand Turismo', 'Corrida', 'PS4')
jogo3 = Jogo('PES2020', 'Futebol', 'PC')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo='jogos do samuel', subTitutlo='rvg', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=["post",])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/autenticar', methods=['post',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash('usuário logado com sucesso')
        return redirect('/')
    else:
        flash('usuário não autenticado')
        redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('usuário deslogado')
    return redirect('/')

#alterando o endereco e porta para iniciar o projeto
#app.run(host='0.0.0.0', port=8080)

app.run(debug=True)