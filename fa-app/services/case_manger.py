from services.dbConnector import DbConn

def create_case(case_data):
    create_case = f"""INSERT INTO BASEAPP.CASE_PROFILE(case_guid,created_by,offence,crime_no,
                                                  log_no,
                                                  _name,
                                                  _rank,
                                                  _no,
                                                  _location,
                                                  vrm,
                                                  make,
                                                  model,
                                                  case_created,
                                                  case_started,
                                                  case_finished,
                                                  module_openandi,
                                                  _description,
                                                  additional_information
                                                  )
                              VALUES ('test_id1','admin','{case_data["offence"]}','{case_data["crime_no"]}',
                              '{case_data["log_no"]}','{case_data["name"]}','{case_data["rank"]}',
                              '{case_data["_no"]}','{case_data["location"]}',
                              '{case_data["vrm"]}','{case_data["make"]}','{case_data["model"]}',
                              '{case_data["case_created"]}','{case_data["case_started"]}','{case_data["case_finished"]}',
                              '{case_data["module_openandi"]}','{case_data["description"]}','{case_data["additional_information"]}'                              
                              );"""
    try:
        pw_conn = DbConn()
        users = pw_conn.writeMan(create_case)
        return users

    except:
        return "User Can't be created"


def get_case_ids():
    case_lists = []
    caseids = "select cid,case_guid from baseapp.case_profile;"
    try:
       conn = DbConn()
       case_lists = conn.queryMan(caseids)
    except Exception as e:
        print(f"Error ocuered due to ,{e}")

    return case_lists


def get_group_info():
    _lists = []
    q = "select gid,g_name from baseapp._groups;"
    try:
       conn = DbConn()
       _lists = conn.queryMan(q)
    except Exception as e:
        print(f"Error ocuered due to ,{e}")
    return _lists

def create_photo_path(data):
    photo_path = f"""INSERT INTO baseapp.photo_path(cid,gid,case_id,group_id,photo_des,file_path,file_name)
                VALUES ('{data["cid"]}','{data["gid"]}','{data["case_id"]}','{data["group_id"]}','{data["photo_des"]}','{data["file_path"]}','{data["file_name"]}');
                """
    try:
        _conn = DbConn()
        db_ack = _conn.writeMan(photo_path)
        print(db_ack)
        return db_ack
    except Exception as e:
        print(e)
        return "User Can't be created"