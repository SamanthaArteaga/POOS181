from flask import Flask, render_template, request, redirect,url_for,flash
from flask_mysqldb import MySQL
app= Flask(__name__)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_floreria'
app.secret_key='mysecretkey'
mysql= MySQL(app)

@app.route('/')
def index():
    CC=mysql.connection.cursor()
    CC.execute('select * from db_floreria')
    conFlores= CC.fetchall()
    print(conFlores)
    return render_template('TablaFloreira.html',listFlores= conFlores)



@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vnombre = request.form['txtNombre']
        Vcantidad = request.form['txtCantidad']
        Vprecio = request.form['txtPrecio']
        (Vnombre,Vcantidad,Vprecio)
    
        CS=mysql.connection.cursor()
        CS.execute('insert into tbflores(nombre,catidad,precio) values (%s,%s,%s)',(Vnombre,Vcantidad,Vprecio)) 
        mysql.connection.commit()

    
    flash('La flor fue agregada completamente')
    return redirect(url_for('TablaFloreria.html'))