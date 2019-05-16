from connect import auth_db
import pandas as pd
from sqlalchemy import create_engine

#credentials = connect.load_auth('read-only')
#user = credentials['username']
#pswd = credentials['password']
#hostname = credentials['host']
#portnum = credentials['port']
#dbname = credentials['database']

#db_string = 'postgresql://'+user+':'+pswd+'@'+hostname+':'+portnum+'/'+dbname
db = create_engine(auth_db())

#FIRST_NAME,LAST_NAME,Home Phone,Cell Phone,EMAIL,PAYMENT,CASH_PRICE,CONTRACT LENGTH,MEMBERSHIP_DESCRIPTION,CLUB_NAME,ENTERDATE
# Create 
# Read

# read enrollments
#result_set = db.execute("SELECT * FROM enrollment_test")  
#result_set = db.execute("SELECT FIRST_NAME, LAST_NAME FROM enrollments")
#sql = "SELECT FIRST_NAME, LAST_NAME FROM enrollments"
sql = "SELECT * FROM enrollments WHERE ENTER_DATE='2019-05-11'"
df = pd.read_sql(sql, db, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
print(df.groupby('club_name')['email'].count().sort_values(ascending=False))
#print('success!')
#row_count=0
#for r in result_set:  
    #print(r)
#    row_count += 1
#print(row_count, 'rows present in query')

# read films
#result_set = db.execute("SELECT * FROM films")  
#for r in result_set:  
#    print(r)

# read enrollments
#result_set = db.execute("SELECT * FROM test_enrollment")  
#for r in result_set:  
#    print(r)
