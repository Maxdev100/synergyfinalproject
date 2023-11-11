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

    # Добавление сотрудника
    def insert_employee(self, name, phone, email, salary):
        try:
            self.cursor.execute('''INSERT INTO Employees (name, phone, email, salary) VALUES (?, ?, ?, ?)''',
                                (name, phone, email, salary))
            self.connection.commit()
            return True
        except:
            messagebox.showerror(title="Ошибка добавления",
                                 message=f"Не удалось добавить сотрудника {name}. Возможно, сотрудник с таким именем уже существует.")
            return False

    # Name - имя пользователя для поиска, soft=False - строгое соответствие имени
    def select_all(self, name=None, soft=False):
        data = None
        if name is None:
            data = self.cursor.execute('''SELECT name, phone, email, salary FROM Employees''').fetchall()
        else:
            if not soft:
                data = self.cursor.execute(
                    f'''SELECT name, phone, email, salary FROM Employees WHERE name="{name}"''').fetchall()
            elif soft:
                data = self.cursor.execute(
                    f'''SELECT name, phone, email, salary FROM Employees WHERE name LIKE "%{name}%"''').fetchall()

        self.connection.commit()
        return data

    # Редактирование данных сотрудника по имени
    def edit(self, name, phone, email, salary):
        self.cursor.execute(f'''UPDATE Employees SET phone=?, email=?, salary=? WHERE name="{name}"''',
                            (phone, email, salary))
        self.connection.commit()

    def delete_by_name(self, name):
        self.cursor.execute(f'''DELETE FROM Employees WHERE name=?''', (name,))
        self.connection.commit()