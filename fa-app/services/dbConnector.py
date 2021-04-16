import psycopg2

class DbConn():
    def __init__(self):
        self.DB = 'fae'
        self.USER = 'docker'
        self.PW = 'docker'
        self.HOST = '172.26.0.2'
        self.PORT = '5432'

    def queryMan(self,sql):
        output = []
        try:
            conn = psycopg2.connect(
               database=self.DB, user=self.USER, password=self.PW, host=self.HOST, port= self.PORT
            )

            conn.autocommit = True
            self.cursor = conn.cursor()
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            print("The number of parts: ", self.cursor.rowcount)


            for row in rows:
                output.append(row)
            self.cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error occuered dueto  : {error}")
        return output

    def writeMan(self, sql):

        try:
            conn = psycopg2.connect(
                database=self.DB, user=self.USER, password=self.PW, host=self.HOST, port=self.PORT
            )

            conn.autocommit = True
            self.cursor = conn.cursor()
            self.cursor.execute(sql)
            return 'OK'
        except (Exception, psycopg2.DatabaseError) as error:
            return f"Error occuered dueto  : {error}"


