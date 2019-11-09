from flask import Flask, render_template
from aluno import Aluno
from avaliacoes import Avaliacoes

aluno1 = Aluno('Bruno', 'Alexandro','bruno','12345')
aluno2 = Aluno('Dyego','Rauen','dyego','54321')

avaliacao1 = Avaliacoes('06/11/2019','Avaliação de matemática','9.5')
avaliacao2 = Avaliacoes('05/12/2019','Avaliação de português','8.5')

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

app.run(debug=True)