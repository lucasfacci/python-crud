import sqlite3
from datetime import datetime, timezone, timedelta

conn = sqlite3.connect("crud.db")
cursor = conn.cursor()

def main():
    table = input("Insira o nome da tabela que você deseja gerenciar (curso ou estudante): ")
    tableLower = table.lower()
    if tableLower == "curso" or tableLower == "estudante":
        action(tableLower)
    else:
        print("Insira uma tabela válida!")


def action(tableLower):
    x = input("Insira qual ação você deseja executar (C, R, U ou D): ")
    xLower = x.lower()
    if tableLower == "curso":
        if xLower == "c":
            c_course()
        elif xLower == "r":
            r_course()
        elif xLower == "u":
            u_course()
        elif xLower == "d":
            d_course()
        else:
            print("Insira uma ação válida!")

    else:
        if xLower == "c":
            c_student()
        elif xLower == "r":
            r_student()
        elif xLower == "u":
            u_student()
        elif xLower == "d":
            d_student()
        else:
            print("Insira uma ação válida!")


def c_course():
    name = input("Insira o nome do curso: ")
    studyArea = input("Insira a área do curso (ex. Humanas, Exatas, Biológicas...): ")

    cursor.execute("INSERT INTO course (name, studyarea) VALUES (?, ?)", (name, studyArea))

    conn.commit()

    print("Dados salvos com sucesso!")


def r_course():
    cursor.execute("""
    SELECT * FROM course;
    """)

    for line in cursor.fetchall():
        print(line)


def u_course():
    update = input("Insira o id do curso a ser atualizado: ")

    cursor.execute(""" SELECT courseid FROM course WHERE courseid == ? """, update)
    checkCourse = cursor.fetchone()

    if checkCourse == None:
        print("Não existe nenhum curso com este id!")
    
    else:
        data = input("Insira qual dado do curso deve ser atualizado (nome ou area): ")

        if data.lower() == "nome":
            newData = input("Insira um novo nome para o curso: ")

            cursor.execute(""" UPDATE course SET name = ? WHERE courseid = ? """, (newData, update))

            conn.commit()

            print("Dado atualizado com sucesso!")

        elif data.lower() == "area":
            newData = input("Insira uma nova área para o curso: ")

            cursor.execute(""" UPDATE course SET studyArea = ? WHERE courseid = ? """, (newData, update))

            conn.commit()

            print("Dado atualizado com sucesso!")

        else:
            print("O dado inserido não existe!")


def d_course():
    delete = input("Insira o id do curso a ser deletado: ")

    cursor.execute(""" SELECT courseid FROM course WHERE courseid == ? """, delete)
    checkCourse = cursor.fetchone()
    cursor.execute(""" SELECT courseid FROM student WHERE courseid == ? """, delete)
    checkStudent = cursor.fetchall()
        
    if checkCourse == None:
        print("Não existe nenhum curso com este id!")

    else:
        if checkStudent != []:
            print("Este curso não pode ser deletado, pois já existem estudantes matriculados!")
       
        else:
            cursor.execute(""" DELETE FROM course WHERE courseid == ? """, delete)

            conn.commit()

            print("O curso foi deletado com sucesso!")


def c_student():
    name = input("Insira o nome do estudante: ")
    dateTimeFunc = datetime.now()
    difference = timedelta(hours = -3)
    timeZoneSP = timezone(difference)
    dateTimeSP = dateTimeFunc.astimezone(timeZoneSP)
    created = dateTimeSP.strftime("%d/%m/%Y %H:%M")
    age = input("Insira a idade do estudante: ")
    cpf = input("Insira o CPF do estudante: ")
    courseIdAux = input("Insira o id do curso do estudante: ")

    cursor.execute("""
    SELECT courseid FROM course WHERE courseid == ?;
    """, courseIdAux)
    courseId = cursor.fetchone()

    if courseId == None:
        print("Não existe nenhum curso com este id!")

    else:
        cursor.execute("INSERT INTO student (courseid, name, created, age, cpf) VALUES (?, ?, ?, ?, ?)", (courseId[0], name, created, age, cpf))
        
        conn.commit()

        print("O estudante foi registrado com sucesso!")


def r_student():
    cursor.execute("""
    SELECT * FROM student;
    """)

    for line in cursor.fetchall():
        print(line)


def u_student():
    update = input("Insira o id do estudante a ser atualizado: ")

    cursor.execute(""" SELECT studentid FROM student WHERE studentid == ? """, update)
    checkStudent = cursor.fetchone()

    if checkStudent == None:
        print("Não existe nenhum estudante com este id!")
    
    else:
        data = input("Insira qual dado do estudante deve ser atualizado (nome, idade ou cpf): ")

        if data.lower() == "nome":
            newData = input("Insira um novo nome para o estudante: ")

            cursor.execute(""" UPDATE student SET name = ? WHERE studentid = ? """, (newData, update))

            conn.commit()

            print("Dado atualizado com sucesso!")

        elif data.lower() == "idade":
            newData = input("Insira uma nova idade para o aluno: ")

            cursor.execute(""" UPDATE student SET age = ? WHERE studentid = ? """, (newData, update))

            conn.commit()

            print("Dado atualizado com sucesso!")

        elif data.lower() == "cpf":
            newData = input("Insira um novo número de cpf para o aluno: ")

            cursor.execute(""" UPDATE student SET cpf = ? WHERE studentid = ? """, (newData, update))

            conn.commit()

            print("Dado atualizado com sucesso!")
            
        else:
            print("O dado inserido não existe!")


def d_student():
    delete = input("Insira o id do estudante a ser deletado: ")

    cursor.execute(""" SELECT studentid FROM student WHERE studentid == ? """, delete)
    checkStudent = cursor.fetchone()

    if checkStudent == None:
        print("Não existe nenhum estudante com este id!")
    
    else:
        cursor.execute(""" DELETE FROM student WHERE studentid == ? """, delete)

        conn.commit()

        print("O estudante foi deletado com sucesso!")


main()