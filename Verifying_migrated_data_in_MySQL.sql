-- 1. Verification for Job table

import pymysql
import cx_Oracle

def get_oracle_conn():
    return cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")

def get_mysql_conn(_db):
    return pymysql.connect(
    host='localhost',
    user='dooo',
    password='1',
    port=3307,
    db=_db,
    charset='utf8')

def compare_rowcount(oracle_rows, mysql_rows):
    print("-- oracle row count =  ", oracle_rows, "-- mysql row count =  ", mysql_rows) 
    if oracle_rows == mysql_rows:
        print("The migration has been successful")
    else:
        print("The migration has been unsuccessful")

def compare_sample(list_mysrow,list_orarow):
    if list_mysrow == list_orarow:
        print("MySQL sample count = ", len(list_mysrow), "Oracle sample count = ", len(list_orarow))
    else:
        print("Fail!")
        print("MySQL sample list = " , list_mysrow)
        print("Oracle sample list = ", list_orarow)


conn_mysql_doodb = get_mysql_conn('doodb')
conn_oracle_doodb = get_oracle_conn()


cur = conn_oracle_doodb.cursor()
sql = "select count(*) from JOBS"
cur.execute(sql)
oracle_rows = cur.fetchone()
cur.close()

cur = conn_mysql_doodb.cursor()
sql = "select count(*) from Job"
cur.execute(sql)
mysql_rows = cur.fetchone()
cur.close()

cur = conn_mysql_doodb.cursor()
sql = "select id, title, min_salary, max_salary from Job order by rand () limit 5"
cur.execute(sql)
mysrow = cur.fetchall()
list_mysrow = list(mysrow)
cur.close()


list_orarow = [] 
cur = conn_oracle_doodb.cursor()
for i in range(5):
    sql = "select JOB_ID, JOB_TITLE, MIN_SALARY, MAX_SALARY from JOBS where JOB_ID = :1"
    # print((mysrow[i][0:],)) 
    
    cur.execute(sql, (mysrow[i][0],))
    orarow = cur.fetchone()
    list_orarow.append(orarow)
cur.close()


compare_rowcount(oracle_rows, mysql_rows)
compare_sample(list_mysrow,list_orarow)
                      
                      
-- 2. Verification for Department table
                      
import pymysql
import cx_Oracle

def get_oracle_conn():
    return cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")

def get_mysql_conn(_db):
    return pymysql.connect(
    host='localhost',
    user='dooo',
    password='1',
    port=3307,
    db=_db,
    charset='utf8')

def compare_rowcount(oracle_rows, mysql_rows):
    print("-- oracle row count =  ", oracle_rows, "-- mysql row count =  ", mysql_rows) 
    if oracle_rows == mysql_rows:
        print("The migration has been successful")
    else:
        print("The migration has been unsuccessful")

def compare_sample(list_mysrow,list_orarow):
    if list_mysrow == list_orarow:
        print("MySQL sample count = ", len(list_mysrow), "Oracle sample count = ", len(list_orarow))
    else:
        print("Fail!")
        print("MySQL sample list = " , list_mysrow)
        print("Oracle sample list = ", list_orarow)


conn_mysql_doodb = get_mysql_conn('doodb')
conn_oracle_doodb = get_oracle_conn()


#with conn_oracle_doodb:

cur = conn_oracle_doodb.cursor()
sql = "select count(*) from DEPARTMENTS"
cur.execute(sql)
oracle_rows = cur.fetchone()
cur.close()


#with conn_mysql_doodb:
cur = conn_mysql_doodb.cursor()
sql = "select count(*) from Department"
cur.execute(sql)
mysql_rows = cur.fetchone()
cur.close()


#with conn_mysql_doodb:
cur = conn_mysql_doodb.cursor()
sql = "select id, name, manager_id from Department order by rand () limit 5"
cur.execute(sql)
mysrow = cur.fetchall()
list_mysrow = list(mysrow)
cur.close()


list_orarow = [] 
#with conn_oracle_doodb:
cur = conn_oracle_doodb.cursor()
for i in range(5):
    sql = "select DEPARTMENT_ID, DEPARTMENT_NAME, MANAGER_ID from DEPARTMENTS where DEPARTMENT_ID = :1"
    # print((mysrow[i][0:],)) 
    
    cur.execute(sql, (mysrow[i][0],))
    orarow = cur.fetchone()
    list_orarow.append(orarow)
cur.close()


compare_rowcount(oracle_rows, mysql_rows)
compare_sample(list_mysrow,list_orarow)
                      
-- 3. Verification for table Employee
-- 4. Verification for table JobHistory
                      
