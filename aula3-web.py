from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/contato')
def contatos():
    return render_template('contato.html')

app.run()