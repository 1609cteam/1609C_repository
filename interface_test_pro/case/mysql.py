import pymysql


def mysql():
    con = pymysql.connect(
                port=3306,
                host='localhost',
                user='root',
                password='lsj',
                db='api_ceshi'
            )
    cur = con.cursor()
    cur.execute('truncate demo_bookinfo')
    con.commit()