#importación del framework
from flask import Flask, render_template, request, redirect,url_for,flash
from flask_mysqldb import MySQL



#Inicialización del APP
app= Flask(__name__)

#Configuración a base de datos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
app.secret_key='mysecretkey'
mysql= MySQL(app)



#Declaración de ruta http://localhost:5000
@app.route('/')
def index():
    CC=mysql.connection.cursor()
    CC.execute('select * from dbalbums')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('index.html',listAlbums= conAlbums)





#ruta http:localhost:5000/guardar tipo POST para insert 
@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']
        (Vtitulo,Vartista,Vanio)
        
        CS=mysql.connection.cursor()
        CS.execute('insert into dbalbums(titulo,artista,anio) values (%s,%s,%s)',(Vtitulo,Vartista,Vanio)) 
        mysql.connection.commit()
    
    flash('El album fue agregado completamente')
    return redirect(url_for('index'))


@app.route('/editar/<id>')
def editar(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM dbalbums WHERE id = %s', (id,))
    album = cursor.fetchone()
    cursor.close()
    return render_template('EditarAlbum.html', album=album)
        
        

@app.route('/Actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varTitulo = request.form['txtTitulo']
        varArtist = request.form['txtArtista']
        varAnio = request.form['txtAnio']

        curAct = mysql.connection.cursor()
        curAct.execute('UPDATE dbalbums SET titulo = %s, artista = %s, anio = %s WHERE id = %s', (varTitulo, varArtist, varAnio, id))
        mysql.connection.commit()
        curAct.close()
        
        flash('Album actualizado: ' + varTitulo)
    return redirect(url_for('index'))


@app.route('/mover/<id>')
def mover(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM dbalbums WHERE id = %s', (id,))
    album = cursor.fetchone()
    cursor.close()
    return render_template('ElimanarAlbum.html', album=album)

@app.route('/Eliminar/<id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()

        if 'confirmar' in request.form:
            cur.execute('DELETE FROM dbalbums WHERE id = %s', (id,))
            mysql.connection.commit()
            flash('Se eliminó de la BD')
        else:
            flash('No se eliminó el álbum')

        cur.close()
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


#Ejecución del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)

