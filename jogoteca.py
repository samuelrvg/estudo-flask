from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')
def ola():
    jogo1 = Jogo('GTA', 'Ação', 'PC')
    jogo2 = Jogo('Grand Turismo', 'Corrida', 'PS4')
    jogo3 = Jogo('PES2020', 'Futebol', 'PC')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='jogos do samuel', subTitutlo='rvg', jogos=lista)

#alterando o endereco e porta para iniciar o projeto
#app.run(host='0.0.0.0', port=8080)

app.run()