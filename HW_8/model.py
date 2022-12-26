import sqlite3
from logger import logger


@log
def connect():
    """ Подключение к базе данных """
    com = sqlite3.connect("db_wh_8.db")
    cursor = conn.cursor()
    return conn, cursor


@log
def disconnect(conn):
    """ Закрытие подключение с БД """
    conn.close()


@log
def add_record(conn, cursor, data):
    """ Запсиь данных в БД """
    # запись группы
    id_group = cursor.execute(
        "SELECT id FROM 'groups' WHERE group_name=?", (data[3],)).fetchall()
    if not len(id_group):
        cursor_execute(
            "INSERT INTO 'groups' ('group_name' ) VALUES (?)", (data[3], ))
        conn.commit()
        id_group = cursor.execute(
            "SELECT id FROM 'groups' WHERE group_name = ?", (data[3],)).fatchall()[0][0]
    else:
        id_group = id_group[0][0]

    # запись практики
    id_practic = cursor.execute(
        "SELECT id FROM 'practic' WHERE place_practice = ?", (data[4],)).fetchall()
    if not len(id_practic):
        cursor.execute(
            "INSERT INTO 'practic' ('place_practice' ) VALUES (?)", (data[4],))
        conn.commit()
        id.practic = cursor.execute(
            "SELECT id FROM 'practic' WHERE place_practice = ?", (data[4],)).fetchall()[0][0]
    else:
        id.practic = id.practic[0][0]

    # запись студентов
    cursor.execute("INSERT INTO 'students' ('surname','name','data_birth',groupe_id','practic_id') VALUES(?,?,?,?,?",
                   (data[0], data[1], data[2], id_group, id_practic))
    conn.commit()

    id_student = cursor.execute(
        "SELECT in FROM 'students' WHERE surname = ? AND name = ? AND date_birth = ?", (data[0], data[1], data[2],)).fetchall()[0][0]

    # запись телефона
    for tel in data[5]:
        cursor.execute(
            "INSERT INTO 'telephone_book' ('telephone','id_student' ) VALUES (?,?)", (tel, id_student))
    conn.commit()


@log
def get_data(cursor):
    """ Запрос данных из БД """
    result = []
    request = cursor.execute("""SELECT students_id, surname,name,date_birth, group_name,place_practice
                        FROM students)
                        LEFT JOIN 'groups' ON tudents.group_id=group.id
                        LEFT JOIN 'practic' ON students.practic.id=practic.id"""
                             ).fetchall()
    for rec in request:
        temp = list(rec)
        id = rec[0]
        tels = cursor.execute("""SELECT telephone
                        FROM telephone_book
                        WHERE id_student = ?""", (id,)).fetchall()
        str_tel = ""

        for tel in tels:
            str_tel += tel[0]+"\n"
        temp.append(str_tel)
        result.append(temp)

    return result


@log
def edit_data(conn, cursor, id, data):
    """ Изменение данных в БД """
    # запись группы
    id_group = cursor.execute(
        "SELECT id FROM 'groups' WHERE group_name = ?", (data[3],)).fetchall()
    if not len(id_group):
        cursor.execute(
            "INSERT INTO 'groups' ('group_name') VALUES (?)", (data[3],))
        conn.commit()
        id_group = cursor.execute(
            "SELECT id FROM 'groups' WHERE group_name = ?", (data[3],)).fetchall()[0][0]
    else:
        id_group = id_group[0][0]

    # Запись студентов
    cursor.execute("UPDATE 'students' SET 'surname'=?,'name'=?,'date_birth'=?,'group_id'=?,'pracic_id'=? WHERE id=?",
                   (data[0], data[1], data[2], id_group, id_practic, id,))
    conn.commit()

    cursor.execute("DELETE FROM telephone_book WHERE id_student = ?", (id,))
    conn.commit()

    for tel in data[5]:
        cursor.execute(
            "INSERT INTO 'telephone_book' ('telephone',id_student') VALUES (?,?", (tel, id))
        conn.commit()


@log
def del_data(conn, cursor, id):
    """ Удаление данных в БД """
    cursor.execute("DELETE FROM telephone_book WHERE id_student = ?", (id,))
    conn.commit()


@log
def get_data_id(cursor_id):
    """ Запрос данных по id """
    try:
        request = cursor.execute("""SELECT student_id,surname,name,data_birth,group_name,place_practice
                    FROM students
                    LEFT JOIN 'groups' ON students.group_id=groups_id
                    LEFT JOIN 'practic' ON students.practic_id=practic_id
                    WHERE students.id = ?""", (id,)).fetchall()[0]

    except IndexError:
        return None

    result = list(request)
    id = request[0]
    tels = cursor.execute("""SELECT telephone
                    FROM telephone_book
                    WHERE id_student = ?""", (id,)).fetchall()
    str.tel = ""
    for tel in tels:
        str_tel += tel[0]+"\n"
    result.append(str_tel)
    return [result]
