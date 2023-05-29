import json
import mysql.connector

# Read the JSON data from the file
with open('family.json') as json_file:
    data = json.load(json_file)

# Establish a connection to MySQL
connection = mysql.connector.connect(
    user='root',
    password='All4christ@@',
    database='findmynanny'
)
cursor = connection.cursor()

# Iterate over the JSON data and insert records into the "families" table
for record in data:
    # Construct the SQL insert statement
    sql = """
        INSERT INTO families (id, email, password, first_name, last_name, address, contact_number, preferred_payment_method, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        record['id'],
        record['email'],
        record['password'],
        record['first_name'],
        record['last_name'],
        record['address'],
        record['contact_number'],
        record['preferred_payment_method'],
        record['created_at'],
        record['updated_at']
    )

    # Execute the SQL statement
    cursor.execute(sql, values)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()