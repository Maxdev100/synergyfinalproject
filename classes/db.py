import sqlite3


# Класс базы данных
class DB:
    def __init__(self):
        # INIT
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

        self.create_table()

    def close_connection(self):
        self.connection.close()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (id PRIMARY KEY, name TEXT, phone TEXT, 
        email TEXT, salary INT)''')
        self.connection.commit()

    def insert_employee(self, name, phone, email, salary):
        self.cursor.execute('''INSERT INTO Employees (name, phone, email, salary) VALUES (?, ?, ?, ?)''',
                            (name, phone, email, salary))
        self.connection.commit()
