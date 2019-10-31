from flask import Flask

app = Flask(__name__)

@app.route('/')
def incio():
     return '<h1> Python </h1>'

@app.route('/cervejas')
def cervejas():
     return '<h1> Cervejas </h1>'

app.run()