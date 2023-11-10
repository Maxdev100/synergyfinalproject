from tkinter import *


class AddWindow:
    # Конструктор класса принимает объект БД
    def __init__(self, db_ex):
        self.db_ex = db_ex

        self.add_window = Tk()
        self.add_window.geometry("400x200")
        self.add_window.title("Добавить пользователя")
        self.add_window.resizable(False, False)
        self.add_window.focus()
