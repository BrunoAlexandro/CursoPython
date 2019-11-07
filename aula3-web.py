from flask import Flask, render_template
from aluno import Aluno
from avaliacoes import Avaliacoes

aluno1 = Aluno()
aluno1.nome = 'Bruno'
aluno1.sobrenome = 'Alexandro'
aluno1.usuario = 'bruno'
aluno1.senha = '12345'

aluno2 = Aluno()
aluno2.nome = 'Dyego'
aluno2.sobrenome = 'Rauen'
aluno2.usuario = 'dyego'
aluno2.senha = '54321'

avaliacao1 = Avaliacoes()
avaliacao1.data = '06/11/2019'
avaliacao1.avaliacao = 'Avaliação de matemática'
avaliacao1.nota = '9.5'

avaliacao2 = Avaliacoes()
avaliacao2.data = '05/12/2019'
avaliacao2.avaliacao = 'Avaliação de português'
avaliacao2.nota = '8.5'

app = Flask(__name__)
nome_pagina = 'Pagina aleatoria'

aluno = [aluno1, aluno2]
avaliacao = [avaliacao1, avaliacao2]

@app.route('/')
def inicio():
    return render_template('home.html', nome=nome_pagina, variavel_aluno = aluno)

@app.route('/contato')
def contatos():
    return render_template('contato.html', nome=nome_pagina, variavel_avaliacao = avaliacao)

app.run()