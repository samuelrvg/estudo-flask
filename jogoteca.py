from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['Mario', 'CS', 'GTA']
    return render_template('lista.html', titulo='Jogos do Samuel', subTitutlo='rvg', jogos=lista)

#alterando o endereco e porta para iniciar o projeto
#app.run(host='0.0.0.0', port=8080)

app.run()