import connect
from sqlalchemy import create_engine

credentials = connect.load_auth('full-access')
user = credentials['username']
pswd = credentials['password']
hostname = credentials['host']
portnum = credentials['port']
dbname = credentials['database']

db_string = 'postgresql://'+user+':'+pswd+'@'+hostname+':'+portnum+'/'+dbname
#engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
db = create_engine(db_string)

# Create 
db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")  
db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")
db.execute("INSERT INTO films (title, director, year) VALUES ('Ironman', 'Someone', '2015')")

# Read
result_set = db.execute("SELECT * FROM films")  
for r in result_set:  
    print(r)

# Update
db.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")

# Delete
db.execute("DELETE FROM films WHERE year='2016'")
