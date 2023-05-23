# Import Third-Party
import psycopg2 as driver

# Import configuration
from config import CONNECTION_STRING


# example table
TABLE_NAME = 'things'


def database_con(conn_string: str): 
    """ create a database connection from a connection string"""
    connection = False
    try:
        connection = driver.connect(conn_string)
    except:
        print('not able to connect to db')

    return connection


def db_execute(conn, query):
    """ execute a given sql-query on connection.cursor() """
    cur = conn.cursor()
    cur.execute(query)
    return cur




def main() -> None:
    conn = database_con(CONNECTION_STRING)
    
    cur = conn.cursor()

    
    # create a example table 
    create_qry = f'CREATE TABLE {TABLE_NAME} (id SERIAL PRIMARY KEY, username VARCHAR(50) NOT NULL)' 
    _ = db_execute(conn, create_qry)
   
    # insert a row into the table
    user_name = 'Wello Horld'
    insert_qry = f"INSERT INTO {TABLE_NAME} (username) VALUES ('{user_name}');"
    _ = db_execute(conn, insert_qry)


    # select all data from the table
    get_qry = f'SELECT * FROM {TABLE_NAME}'
    cur = db_execute(conn, get_qry)
   

    # fetch the data from the cursor
    result = cur.fetchall() 
    print(result)


if __name__ == "__main__":
    main()

