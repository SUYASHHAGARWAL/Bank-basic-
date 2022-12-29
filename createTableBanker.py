import pymysql as SQL

try:


    conn=SQL.connect(host='localhost',port=3306,user='root',passwd='1234',database='bank')
    smt=conn.cursor()
    q="create table banker(acountnum int primary key auto_increment,name varchar(30),balance decimal(8,4),mobile decimal(10))"
    smt.execute(q)
    print("Table created successfully")
    conn.commit()
    conn.close()

except Exception as err:
    print("Error",err)