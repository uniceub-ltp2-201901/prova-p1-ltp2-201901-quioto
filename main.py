# Importando bibliotecas
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *





app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade'


@app.route('/')
def principal():
    cursor= mysql.get_db().cursor()
    return render_template('professores.html', professores=listar_professores(cursor))



@app.route('/detalhar/<listarprofessores>')
def detalhar(listarprofessores):
    cursor= mysql.get_db().cursor()
    return render_template('disciplina.html', detalhe=exibir_professores(cursor, nome=listarprofessores))

@app.route('/consulta', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        titulacao = request.form.get('titulacao')



        cursor = mysql.get_db().cursor()


        idtitulacao = get_titu(cursor, titulacao)




        if idtitulacao is None:
            return render_template('professores.html', erro='algo de errado não está certo')
        else:

            cursor = mysql.get_db().cursor()

            return render_template('consulta.html', nome=titulacao, consulta=exibir_professores(cursor, nome=listar_professores))

    else:
        return render_template('index.html', erro='Método incorreto. Use POST!')


if __name__ == '__main__':
    app.run(debug=True)






