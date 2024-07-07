import mysql.connector
 
# First of all, lets establish the connection to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ss@12345",
    database="relational data model for youtube"
)

# Let's create a cursor object
cursor = db_connection.cursor()
# Let's define a function
# Let's define a function to count the number of rows in each table
def count_rows(table_name):
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchone()
    print(f"Number of rows in {table_name}: {result[0]}")
 
# Let's define a function to display a sample of 3 rows from each table
def display_sample_rows(table_name):
    query = f"SELECT * FROM {table_name} LIMIT 3"
    cursor.execute(query)
    result = cursor.fetchall()
    print(f"\nSample rows from {table_name}:")
    for row in result:
        print(row)
 
# Let's define a function to join two tables and display data
def join_tables(table1, table2, table1_column, table2_column):
    query = f"""
    SELECT *
    FROM {table1}
    JOIN {table2} ON {table1}.{table1_column} = {table2}.{table2_column}
    LIMIT 3
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print(f"\nJoined data from {table1} and {table2}:")
    for row in result:
        print(row)
 
# This is my List of tables
tables = ["Channels", "Videos", "Playlists", "Comments"]
 
query = f"SELECT Channels.*, Videos.* FROM Channels JOIN Videos ON Channels.channel_id = Videos.channel_id"

# Task-1, Let's count the number of rows and for Task-2 display sample rows from each table
for table in tables:
    count_rows(table)
    display_sample_rows(table)
 
# Task-3, Let's perform a join between Channels and Videos using the primary and foreign key relationship
join_tables("Channels", "Videos", "channel_id", "channel_id")
 
# This is the end, let's Close the cursor and the connection
cursor.close()
db_connection.close() 
