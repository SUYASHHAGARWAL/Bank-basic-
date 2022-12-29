import pymysql as SQL

try:

    conn=SQL.connect(host='localhost',port=3306,user='root',passwd='1234')
    smt=conn.cursor()
    q="create database bank"
    smt.execute(q)
    print("Database created successfully")
    conn.commit()
    conn.close()

except Exception as err:
    print("Error",err)