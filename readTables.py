from connect import auth_db
from sqlalchemy import create_engine

db = create_engine(auth_db())

# read enrollments
result_set = db.execute("SELECT FIRST_NAME, LAST_NAME FROM enrollments")

#print('success!')
row_count=0
for r in result_set:  
    row_count += 1
print(row_count, 'rows present in query')
