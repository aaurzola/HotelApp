from flask import request, Flask,flash, render_template, jsonify, url_for
import flask
import crudHabitacion as bd
from settings.config import configuracion
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
app.config.from_object(configuracion)


@app.route('/')
def index():
    return render_template('index.html', titulo="Ejemplo Hotel Gevora")

@app.route('/homeProfile')
def hprofile():
    return render_template('homeProfile.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/myProfile')
def mprofile():
    return render_template('myprofile.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/admo_hab')
def admohab():
    lista = bd.sql_select_habitaciones()
    
    return render_template('admo_hab.html',l_hab=lista, titulo="Ejemplo Hotel Gevora 2")

@app.route('/historialReserva')
def historeserva():
    return render_template('historialReserva.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/login')
def login():
    return render_template('login.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/SignUp')
def signup():
    return render_template('SignUp.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/Vista_admin_usuarios')
def vistaadminusuarios():
    return render_template('Vista_admin_usuarios.html', titulo="Ejemplo Hotel Gevora 2")

app.run(debug=True)







