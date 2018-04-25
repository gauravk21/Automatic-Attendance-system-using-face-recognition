import mysql.connector
from mysql.connector import Error
import pymysql



def connect( name ,college):
    """ Connect to MySQL database """
    try:
        conn = pymysql.connect(host='192.168.115.1',
                                       database='face_rec_db',
                                       user='dbuser',
                                       password='root1234')

        print('Connected to MySQL database')
        cursor = conn.cursor()
        # sql = """INSERT INTO basic_ivo(id, name, college) VAlUES (4 , 'PRITAM' , 'SKN')"""
        # try:
        #
        #     cursor.execute(sql)
        #     print(" A row is inserted")
        #     conn.commit()
        #
        #
        # except:
        #     conn.rollback()
        #     print("error")

        sql2 = " SELECT `id`, `college` FROM basic_ivo  WHERE `name` = 'SHARDUL'"
        try:
            # cursor.execute(sql2)
             #print("ID: %s -- College : %s" % cursor.fetchone())
            data = ( name , college )
            sql3 = " UPDATE basic_ivo SET name = %s , `college` = %s WHERE id = 3 "
            cursor.execute(sql3, data)
            print('successful')
        except:
             print('error')







   # """INSERT INTO EMPLOYEE(FIRST_NAME,
      # LAST_NAME, AGE, SEX, INCOME)
       #VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""


    except Error as e:
        print(e)

    #finally:
    conn.close()


if __name__ == '__main__':
    connect('NEERAJ', 'SCOE')