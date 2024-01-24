import random
from datetime import datetime, timedelta
import mysql.connector

# Replace these with your MySQL credentials
db_config = {
    'host': 'localhost',
    'user': 'OjasvaSingh',
    'password': 'vishusingh',
    'database': 'bg',
    'auth_plugin': 'mysql_native_password'
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

id = 1
# Generate and insert 10,000 rows of data
for _ in range(1,10001):
    uid = 'user_' + str(_).zfill(4)
    name = 'User ' + str(random.randint(1, 10001))
    score = random.randint(0, 100)
    country = random.choice(['US', 'CA', 'GB', 'IN', 'AU'])
    timestamp = datetime.now() - timedelta(days=random.randint(0, 365))

    # SQL query to insert data
    insert_query = "INSERT INTO Leaderboard (UID, Name, Score, Country, TimeStamp) VALUES (%s, %s, %s, %s, %s)"
    data = (uid, name, score, country, timestamp)

    cursor.execute(insert_query, data)
    id = id+1

# Commit changes and close the connection
connection.commit()
connection.close()
