from services.dbConnector import DbConn
import ast

def create_group(data):
    q = f"""INSERT INTO baseapp._groups(g_name,g_des)
                    VALUES ('{data["gnm"]}','{data["gdes"]}');                 """
    try:
        _conn = DbConn()
        db_ack = _conn.writeMan(q)
        print(db_ack)
        return db_ack
    except Exception as e:
        print(e)
        return "Group Can't be created"

def create_feedback(data):

    q = f"""INSERT INTO baseapp.t_feedback(cid,gid,student_id,grade,feedback)
                        VALUES ('{ast.literal_eval(data["cid"])[0]}','{ast.literal_eval(data["gid"])[0]}','{data["student_id"]}','{data["grade"]}','{data["feedback"]}');                 """
    try:
        _conn = DbConn()
        db_ack = _conn.writeMan(q)
        print(db_ack)
        return db_ack
    except Exception as e:
        print(e)
        return "Feedback Can't be created"


def get_greades():
    _lists = []
    q = "select distinct grade from baseapp.t_grades ORDER BY grade;"
    try:
       conn = DbConn()
       _lists = conn.queryMan(q)
    except Exception as e:
        print(f"Error ocuered due to ,{e}")
    return _lists

def get_students():
    _list = []

    q ="SELECT * FROM baseapp.t_student;"
    try:
        conn = DbConn()
        _lists = conn.queryMan(q)
    except Exception as e:
        print(f"Error ocuered due to ,{e}")
    return _lists



