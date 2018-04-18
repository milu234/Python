import mysql.connector;
conn=mysql.connector.connect(host='localhost',database='world',user='root',password='jordanbelfort@123')
cursor=conn.cursor()

def update_rows(eno):
    str="update emptab set sal=sal+1000 where eno='%d'"
    args=(eno)
    try:
        cursor.execute(str%args)
        conn.commit()
        print("1 row updated")
    except:
        conn.rollback()

    cursor.close()
    conn.close()

x=int(input("Enter the Employee no: you want to update : "))
update_rows(x)
