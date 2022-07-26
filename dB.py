import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con=sqlite3.connect('luna.db')
        return con
    except Error:
        print(Error)

def sql_select_all_ReservaU(username):
    strsq="SELECT * FROM Reservas WHERE IdUsuario ='"+ username +"';"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsq)
    reservas = cursor_Obj.fetchall()
    con.close()
    return reservas

def sql_select_Reserva_all():
    strsq="SELECT * FROM Reservas;"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsq)
    reservas = cursor_Obj.fetchall()
    con.close()
    return reservas

def sql_select_Reserva_byId(id):
    strsq="SELECT * FROM Reservas WHERE IdUsuario ='"+ id +"';"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsq)
    reservas = cursor_Obj.fetchall()
    con.close()
    return reservas

def sql_edit_rate_reserva(id, rate, comentario):
    strsql='UPDATE Reservas SET Calificacion = ?, Comentario = ? WHERE Id = ?;'
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql, (int(rate), comentario, int(id)))
    con.commit()
    con.close()

def sql_update_reserva(id, FechaInicio, FechaFinal, room, estado, costo,): 
    strsql='UPDATE Reservas SET FechaInicio = ?, FechaFinal = ?, IdHab = ?, costo = ?, Estado = ? WHERE Id = ?;'
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql, ( FechaInicio, FechaFinal,room,costo, estado,id))
    con.commit()
    con.close()

def sql_add_reservas(FechaInicio, FechaFinal, costo, Estado,user):
    dreamer = "INSERT INTO Reservas (FechaInicio, FechaFinal, costo, Estado, IdUsuario) VALUES(?, ?, ?, ?, ?);"
    con = sql_connection()
    cursor_Obj = con.cursor()   
    print(FechaInicio)
    cursor_Obj.execute(dreamer,(FechaInicio, FechaFinal, costo, Estado, user))
    con.commit()
    con.close()

def sql_insert_reservas(FechaInicio, FechaFinal, room, costo, estado, user):
    strsql = "INSERT INTO Reservas (FechaInicio, FechaFinal, IdHab, costo, Estado, IdUsuario) VALUES(?, ?, ?, ?, ?, ?);"
    con = sql_connection()
    cursor_Obj = con.cursor()   
    print(FechaInicio)
    cursor_Obj.execute(strsql,(FechaInicio, FechaFinal, room, costo, estado, user))
    con.commit()
    con.close()

def sql_add_habitacion(id, estado, valor):
    try:  # me conecto a la base de datos
        con = sql_connection()
        # creo un cursor para poder ejecutar las consultas
        cursor_Obj = con.cursor()
        # creo la consulta para insertar una habitacion
        strsql = "INSERT INTO Habitaciones (Id, Estado, Precio) VALUES(?,?,?);"
        print(strsql)
        valores = (id, estado, valor)
        # ejecuto la consulta
        cursor_Obj.execute(strsql, (valores))
        con.commit()
    except Error as e:
        # si hay algun error lo muestro y retorno None
        print(e)
        return None
    finally:
        # cierro la conexion a la base de datos
        con.close()
        
    return cursor_Obj.lastrowid # retorno el id de la habitacion insertada
#------------------------------------------------------------------------------------------------------------------
def sql_crear_tabla_habitaciones():
    strsql = "CREATE TABLE IF NOT EXISTS Habitaciones (Id INTEGER PRIMARY KEY, Estado TEXT);"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()
#------------------------------------------------------------------------------------------------------------------
def sql_update_habitacion(id, Nestado, valor):
    strsql = 'UPDATE Habitaciones SET Estado = ?, Precio =? WHERE Id = ?;'
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql, (Nestado, valor, id))
    con.commit()
    con.close()
#------------------------------------------------------------------------------------------------------------------
def sql_delete_habitacion(id):
    strsql = "DELETE FROM Habitaciones WHERE Id = "+id+";"
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    con.commit()
    con.close()
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitaciones():
    strsql = "SELECT * FROM Habitaciones;"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitaciones = cursor_Obj.fetchall()
    con.close()
    return habitaciones
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitacion(id):
    strsql = "SELECT * FROM Habitaciones WHERE Id = "+id+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitacion_estado(estado):
    strsql = "SELECT * FROM Habitaciones WHERE Estado = "+estado+";"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitacion_estado_disponible():
    strsql = "SELECT * FROM Habitaciones WHERE Estado = 'Disponible';"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitacion_estado_ocupada():
    strsql = "SELECT * FROM Habitaciones WHERE Estado = 'Ocupada';"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion
#------------------------------------------------------------------------------------------------------------------
def sql_select_habitacion_estado_reservada():
    strsql = "SELECT * FROM Habitaciones WHERE Estado = 'Reservada';"
    print(strsql)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    habitacion = cursor_Obj.fetchall()
    con.close()
    return habitacion

def sql_delete_reserva(id):
    eros = "DELETE FROM Reservas WHERE Id = "+id+";"
    print(eros)
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(eros)
    con.commit()
    con.close()
#----------------------New users--------------------------------------------------------
def sql_select_usuarios():
    strsql = "SELECT * FROM Usuarios;"
    con = sql_connection()
    cursor_Obj = con.cursor()
    cursor_Obj.execute(strsql)
    users =cursor_Obj.fetchall()
    con.close()
    return users

def sql_select_all_usuario(username):
    strsq="SELECT * FROM Usuarios WHERE Email ='"+ username +"';"
    # strsq="SELECT * FROM Usuarios WHERE Email ='cway@outlook.com';"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsq)
    usuario = cursor_Obj.fetchone()
    con.close()
    return usuario

def sql_select_usuario_all(username):
    strsq="SELECT * FROM Usuarios WHERE Email ='"+ username +"';"
    # strsq="SELECT * FROM Usuarios WHERE Email ='cway@outlook.com';"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsq)
    usuario = cursor_Obj.fetchall()
    con.close()
    return usuario

def sql_insert_user_new(Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Rol, tel):
    con = sql_connection()
    cursor_Obj = con.cursor()
    datura = "INSERT INTO Usuarios (Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Telefono, Rol) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
    print(Email)
    cursor_Obj.execute(datura,(Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, tel, Rol))
    con.commit()
    con.close()

def sql_delete_usuario(username):
    strsql="DELETE FROM Usuarios WHERE Email = ?;"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,(username,))
    con.commit()
    con.close()

def sql_update_usuario(name, lastname, username, tel, sex, birddate, rol):
    strsql='UPDATE Usuarios SET  Nombres = ?, Apellidos = ?,  Genero = ?, FechadeNacimiento = ?, Telefono = ?, Rol = ? WHERE Email = ?;'
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,(name, lastname, sex, birddate, tel, rol, username))
    con.commit()
    con.close()

def sql_insert_user(Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Rol):
    con = sql_connection()
    cursor_Obj = con.cursor()
    datura = "INSERT INTO Usuarios (Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Rol) VALUES(?, ?, ?, ?, ?, ?, ?);"
    print(Email)
    cursor_Obj.execute(datura,(Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Rol))
    con.commit()
    con.close()

def sql_auth_user(username, password):
    strsq="SELECT * FROM Usuarios WHERE Email = ? AND Contraseña =?;"
    # strsq="SELECT * FROM Usuarios WHERE Email ='cway@outlook.com';"
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsq,(username, password))
    usuario = cursor_Obj.fetchall()
    con.close()
    return usuario

def sql_edit_usuario(name, lastname, username, tel, sex, birddate):
    strsql='UPDATE Usuarios SET  Nombres = ?, Apellidos = ?,  Genero = ?, FechadeNacimiento = ?, Telefono = ? WHERE Email = ?;'

    print(birddate)
    con=sql_connection()
    cursor_Obj=con.cursor()
    cursor_Obj.execute(strsql,(name, lastname, sex, birddate, tel, username))
    con.commit()
    con.close()


