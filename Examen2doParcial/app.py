from flask import Flask, render_template, request, redirect,url_for,flash
from flask_mysqldb import MySQL
app= Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_floreria'
app.secret_key='mysecretkey'
mysql= MySQL(app)

@app.route('/')
def index():
    CC=mysql.connection.cursor()
    CC.execute('select * from tbflores')
    conFlores= CC.fetchall()
    print(conFlores)
    return render_template('TablaFloreria.html',listFlores= conFlores)



@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vnombre = request.form['txtNombre']
        Vcantidad = request.form['txtCantidad']
        Vprecio = request.form['txtPrecio']
        (Vnombre,Vcantidad,Vprecio)
    
        CS=mysql.connection.cursor()
        CS.execute('insert into tbflores(nombre,cantidad,precio) values (%s,%s,%s)',(Vnombre,Vcantidad,Vprecio)) 
        mysql.connection.commit()

    
    flash('La flor fue agregada completamente')
    return redirect(url_for('index'))


@app.route('/mover/<id>')
def mover(id):
   cursorID=mysql.connection.cursor()
   cursorID.execute('select * from tbflores WHERE id = %s', (id))
   consulID= cursorID.fetchone()
   return render_template('EliminarFlor.html',flor=consulID)



@app.route('/Eliminar/<id>',methods=['POST'])
def eliminar(id):

    if request.method == 'POST':
        eliNombre=request.form['txtNombre']
        eli=request.form['txtCantidad']
        elianio=request.form['txtPrecio']

        curEli= mysql.connection.cursor()
        curEli.execute('delete from tbflores  where id= %s',(id))
        mysql.connection.commit()

    if 'confirmar' in request.form: 
            curEli = mysql.connection.cursor()
            curEli.execute('DELETE FROM tbflores WHERE id = %s', (id,))
            mysql.connection.commit()
            flash('Se eliminó de la BD: ' + eliNombre)
    else:
            flash('No se eliminó la flor:' + eliNombre)
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
