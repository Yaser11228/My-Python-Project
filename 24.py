# Create a class Database that connects to a database and provides methods to execute queries. Handle exceptions if the connection fails.
import sqlite3


class Database:
    def __init__(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            print(f"Connection failed: {e}")

    def execute_query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Query failed: {e}")