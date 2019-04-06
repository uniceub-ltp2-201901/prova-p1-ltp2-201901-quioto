def listar_professores(cursor):

    cursor.execute(f'select professor.nome from faculdade.professor')


    professores = cursor.fetchall()


    cursor.close()


    return professores

def exibir_professores(cursor, nome):

    cursor.execute(f'select nome, datanasc, nomemae, titulacao from faculdade.professor where nome = "{nome}"')

    a = cursor.fetchone()
    cursor.close()

    return a

def get_titu(cursor, titulacao):
    cursor.execute(f'select titulacao from faculdade.professor where titulacao')

    consulte = cursor.fetchall()

    cursor.close()

    return consulte





# def get_disciplina(cursor):
#
#     cursor.execute(f'select disciplina.nome from faculdade.disciplina')
#
#     disciplina = cursor.fetchall()
#
#     cursor.close()
#
#     return disciplina