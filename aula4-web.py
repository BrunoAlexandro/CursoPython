from flask import Flask, render_template, request

nome_pagina = 'Pizzaria'
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', pagina = nome_pagina)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', cadastrar = nome_pagina)


#request do import, serve para dar request em algo que foi inserido no html.
@app.route('/salvar')
def salvar():
    sabores = request.args["sabores"]
    tamanho = request.args["tamanho"]
    endereco = request.args["endereco"] 
    with open('pizzas.txt', 'a') as arquivo:
        arquivo.write(f'{sabores};{tamanho};{endereco}')
    return 'Cadastro salvo, ' 


app.run(debug=True)