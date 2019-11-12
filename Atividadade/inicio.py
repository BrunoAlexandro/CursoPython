from flask import Flask, render_template, request, redirect
from aula5 import Carro

pagina = 'Cadastro de carro'
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('cadastro_carro.html', pagina = pagina)

@app.route('/salvar')
def cadastar():
    modelo = request.args['modelo']
    ano = request.args['ano']
    marca = request.args['marca']
    categoria = request.args['categoria']
    
    carro = Carro(modelo, ano, marca, categoria)
    
    with open('carros.txt', 'a') as arquivo:
        arquivo.write(f'{carro.modelo};{carro.ano};{carro.marca};{carro.categoria}\n')
        return redirect('/')

@app.route('/salvos')
def salvos():
    lista_carros = []
    with open('carros.txt', 'r') as arquivocarro:
        for c in arquivocarro:
            vetor = c.strip().split(';')
            carro = carro(c[0], [1], [2])
            lista_carros.append(vetor)
        return render_template('salvos.html', lista = lista_carros)


app.run(debug=True)
