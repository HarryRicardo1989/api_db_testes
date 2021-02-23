import mariadb
import dbAccount as db
import datetime as dt


class DATABASE:
    def __init__(self):
        self .connect = mariadb.connect(
            user=db.user,
            password=db.password,
            host=db.host,
            database=db.database
        )
        pass

    def insert_DB(self, hostname, data_hora, angulo, temperatura):

        conn = self.connect
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO ada_testes_temperatura_tbl ( hostname, data_hora, angulo, temperatura) VALUES (?, ?, ?, ?)",
                        (hostname, data_hora, angulo, temperatura))
            print("ok")
        except mariadb.Error as e:
            print(f'Error: {e}')
        conn.commit()
        conn.close()

    def select_DB(self, horas_de_coleta=1.0):
        timedelta = dt.timedelta(hours=horas_de_coleta)
        data = dt.datetime.now() - timedelta
        tempo = data.strftime("%Y-%m-%d %H:%M:%S")
        conn = self.connect
        cur = conn.cursor()
        cur.execute(f'SELECT hostname, data_hora, angulo, temperatura FROM ada_testes_temperatura_tbl where data_hora > "{tempo}" order by data_hora desc;')
        # cur.execute(f'SELECT * FROM ada_testes_temperatura_tbl order by ID desc')
        row_list = []
        print(row_list)
        for data in cur:
            row_list.append(data)

        conn.commit()
        conn.close()
        return row_list

print(DATABASE().select_DB(6))
    


""" for item in DATABASE().min_max_med_hora_DB(2):
    print(item) """
