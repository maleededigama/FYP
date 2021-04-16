from services.dbConnector import DbConn

class User:
    def check_user_pw(self,user_pw,email):

        pw_query = f"SELECT email,pw FROM baseapp.appuser WHERE pw = crypt('{user_pw}', pw);"
        pw_conn = DbConn()
        users = pw_conn.queryMan(pw_query)
        print(users)
        if len(users) > 0 :
            for user in users:
                if str(email).lower().strip() == user[0].lower().strip() :
                    print("User Validated")
                    return True
        else:
            return False

class UserAct:

    def create_user(self,data):

        create_user = f"""INSERT INTO BASEAPP.APPUSER(email,fname,lname,pw,active)
                          VALUES ('{data["email"]}','{data["fname"]}','{data["lname"]}',crypt('malpw', gen_salt('bf')) , 1);"""

        try:
            pw_conn = DbConn()
            users = pw_conn.writeMan(create_user)
            return users

        except:
            return "User Can't be created"





