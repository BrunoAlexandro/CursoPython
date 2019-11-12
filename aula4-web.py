from flask import Flask, render_template, request

nome_pagina = 'Pizzaria'
app = Flask(__name__)

@app.route('/')
def inicio():
   lista_pizzas = []
    #A função with serve para fechar a função automaticamente, sem usar o close.
    #'r' é para ler o arquivo(modo de leitura).
   with open('pizzas.txt', 'r') as arquivopizzas:
        for l in arquivopizzas:
            quebralinha = l.split(';')#Split serve para quebrar a linha, por exemplo ponto e vírgula.
            lista_pizzas.append(quebralinha)
            # sabores = quebralinha [0]
            # tamanhos = quebralinha [1]
            # endereco = quebralinha [2]
        return render_template('index.html', pagina = nome_pagina, lista = lista_pizzas)

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
        arquivo.write(f'{sabores};{tamanho};{endereco}\n')
    return 'Cadastro salvo, ' 


app.run(debug=True)