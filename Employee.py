import mysql.connector;
conn=mysql.connector.connect(host='localhost',database='world',user='root',password='jordanbelfort@123')
if conn.is_connected():
    print("Connected to MySql Database")
    cursor=conn.cursor()
    cursor.execute("select * from emptab;")
    row=cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fetchone()
cursor.close
conn.close()
                   
                
