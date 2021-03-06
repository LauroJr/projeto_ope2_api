import sqlite3
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuração

'''
DATABASE = './tmp/flaskr.db'
DEBUG = False
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
'''

# criar nossa pequena aplicação :)
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    msg = "Faça seu login aqui"
    return render_template('login.html', msg=msg)

@app.route('/clientes')
def cliente():
    msg = "Tela dos dados Cliente"
    return render_template('clientes.html', msg=msg)

if __name__ == '__main__':
    app.debug = True
    app.run()
