import sqlite3
from tkinter import messagebox


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
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (id INTEGER PRIMARY KEY, name TEXT UNIQUE, phone TEXT, 
        email TEXT, salary INT)''')
        self.connection.commit()

    def insert_employee(self, name, phone, email, salary):
        try:
            self.cursor.execute('''INSERT INTO Employees (name, phone, email, salary) VALUES (?, ?, ?, ?)''',
                                (name, phone, email, salary))
        except:
            messagebox.showerror(title="Ошибка добавления",
                                 message=f"Не удалось добавить сотрудника {name}. Возможно, сотрудник с таким именем уже существует.")

        self.connection.commit()

    def select_all(self):
        data = self.cursor.execute('''SELECT name, phone, email, salary FROM Employees''').fetchall()
        self.connection.commit()
        return data
