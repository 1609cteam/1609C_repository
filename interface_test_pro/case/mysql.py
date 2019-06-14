import pymysql


def mysql():
    con = pymysql.connect(
        port=3306,
        host='localhost',
        user='root',
        password='123',
        db='yy'
    )
    cur = con.cursor()
    cur.execute('SET foreign_key_checks=0')
    cur.execute('truncate demo_ban')
    cur.execute('SET foreign_key_checks=1')
    con.commit()
# 清空表操作
