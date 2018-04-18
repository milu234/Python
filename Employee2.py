import mysql.connector;
conn=mysql.connector.connect(host='localhost',database='world',user='root',password='jordanbelfort@123')
cursor=conn.cursor()
def del_rows(eno):
    str="delete from emptab where eno = '%d'"
    args=(eno)
    try:
        
          
          cursor.execute(str%args)
          conn.commit()
          print("i row Deleted")
          
        
        
    except:
        conn.rollback()

    cursor.close()
    conn.close()

        
x=int(input("Enter Employee no : "))
del_rows(x)
        
