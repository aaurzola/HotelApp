from flask_wtf import Form, FlaskForm
from wtforms.fields import DateField
from wtforms import StringField,  PasswordField, SubmitField, SelectField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired

class Habitacion(FlaskForm):
    idHab = StringField('idHab', validators=[DataRequired()])
    acc = StringField('acc', validators=[DataRequired()])
    estado = StringField('estado', choices=[('Disponible', 'Disponible'),('Ocupada', 'Ocupada'),('Reservada', 'Reservada'),('Mantenimiento', 'Mantenimiento')], validators=[DataRequired()])
    
class loginForm(Form):
    username = EmailField('username', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    send = SubmitField('Ingresar')

class profileform(Form):
    name = StringField('Nombres:', validators=[DataRequired()])
    lastname = StringField('Apellidos:', validators=[DataRequired()])
    sex = SelectField('Sexo:', choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre'), ('Otro', 'Otro')], validators=[DataRequired()])
    address = StringField('Direccion:', validators=[DataRequired()])
    tel = StringField('Telefono:', validators=[DataRequired()])
    birddate = DateField('Fecha de nacimiento:', validators=[DataRequired()])
    username = EmailField('Correo:', validators=[DataRequired()])
    contra = PasswordField('Contraseña')
    send = SubmitField('Actualizar')

class admUsers(Form):
    name = StringField('Nombres:', validators=[DataRequired()])
    lastname = StringField('Apellidos:', validators=[DataRequired()])
    sex = SelectField('Sexo:', choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre'), ('Otro', 'Otro')], validators=[DataRequired()])
    address = StringField('Direccion:', validators=[DataRequired()])
    tel = StringField('Telefono:', validators=[DataRequired()])
    birddate = DateField('Fecha de nacimiento:', validators=[DataRequired()])
    username = EmailField('Correo:', validators=[DataRequired()])
    contra = PasswordField('Contraseña')
    rol = SelectField('Genero:', choices=[('Usuario', 'Usuario'), ('Administrador', 'Administrador'), ('Superadministrador', 'Superadministrador')], validators=[DataRequired()])
    send = SubmitField('Actualizar')
    delete = SubmitField('Eliminar')

class admUsersIni(Form):
    name = StringField('Nombres:')
    lastname = StringField('Apellidos:')
    sex = SelectField('Sexo:', choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre'), ('Otro', 'Otro')])
    address = StringField('Direccion:')
    tel = StringField('Telefono:')
    birddate = DateField('Fecha de nacimiento:')
    username = EmailField('Correo:')
    contra = PasswordField('Contraseña')
    rol = SelectField('Genero:', choices=[('Usuario', 'Usuario'), ('Administrador', 'Administrador'), ('Superadministrador', 'Superadministrador')])
    send = SubmitField('Actualizar')
    delete = SubmitField('Eliminar')

class rateform(Form):
    IdReserva = StringField('IdReserva', validators=[DataRequired()])
    rate = StringField('Rate', validators=[DataRequired()])
    comentario = StringField('Comentario:', validators=[DataRequired()])
    send = SubmitField('Guardar')

class Usuarios(Form):
    name = StringField('Nombres:', validators=[DataRequired()])
    lastname = StringField('Apellidos:', validators=[DataRequired()])
    sex = SelectField('Sexo:', choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre'), ('Otro', 'Otro')], validators=[DataRequired()])
    contra = PasswordField('Contraseña', validators=[DataRequired()])
    birddate = DateField('FechadeNacimiento:', validators=[DataRequired()])
    email = EmailField('Correo Electronico:', validators=[DataRequired()])
    rol = SelectField('Genero:', choices=[('Usuario', 'Usuario'), ('Administrador', 'Administrador'), ('Superadministrador', 'Superadministrador')], validators=[DataRequired()])
    signup = SubmitField('Registrar')

class Reservas(Form):
    daterbird = DateField('FechaFinal:', validators=[DataRequired()])
    costo = SelectField('Costo:', choices=[('$150', '$150')], validators=[DataRequired()])
    estado = SelectField('Estado:', choices=[('Activa', 'Activa'), ('Cancelada', 'Cancelada'), ('Finalizada', 'Finalizada')], validators=[DataRequired()])
    birddate = DateField('FechaInicio:', validators=[DataRequired()])
    buy = SubmitField('Comprar')

class admReservas(Form):
    id = StringField('Id')
    username = EmailField('Correo Electronico:', validators=[DataRequired()])
    checkin = DateField('FechaInicio:', validators=[DataRequired()])
    checkout = DateField('FechaFinal:', validators=[DataRequired()])
    room = StringField('Habitacion')
    estado = SelectField('Estado:', choices=[('Activa', 'Activa'), ('Cancelada', 'Cancelada'), ('Finalizada', 'Finalizada')], validators=[DataRequired()])
    costo =StringField('Costo', validators=[DataRequired()])
    buy = SubmitField('Comprar')
