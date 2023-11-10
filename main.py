from tkinter import *
from classes.db import *


class MainWindow:
    def __init__(self):
        # Создание окна
        self.app = Tk()
        self.app.title("Список сотрудников компании")
        self.app.geometry("650x500")
        self.app.resizable(False, False)
        self.app.protocol("WM_DESTROY_WINDOW", exit)

        # Цикл приложения
        self.app.mainloop()

    # Выход из программы
    def exit(self):
        db.close_connection()
        self.app.destroy()


# Старт программы
if __name__ == "__main__":
    db = DB()  # Создание БД
    db.insert_employee("Vasa", "8805553535", "vasya@gmail.com", 72440)
    main_window = MainWindow()
