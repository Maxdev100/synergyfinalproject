from tkinter import *
from tkinter import messagebox


class AddWindow:
    # Конструктор класса принимает объект БД
    def __init__(self, db_ex, mainwindow_ex):
        self.db_ex = db_ex
        self.mainwindow_ex = mainwindow_ex
        self.font = "Arial 14"

        # Инициализация окна
        self.add_window = Toplevel()
        self.add_window.geometry("470x170")
        self.add_window.title("Добавить сотрудника")
        self.add_window.resizable(False, False)
        self.add_window.focus()

        # Создание текстовых меток, кнопки и полей ввода
        Label(self.add_window, text="ФИО", font=self.font).place(x=5, y=5)
        Label(self.add_window, text="Телефон", font=self.font).place(x=5, y=35)
        Label(self.add_window, text="Электронная почта", font=self.font).place(x=5, y=65)
        Label(self.add_window, text="Зарплата", font=self.font).place(x=5, y=95)

        self.name = Entry(self.add_window, width=25, font=self.font)
        self.phone = Entry(self.add_window, width=25, font=self.font)
        self.email = Entry(self.add_window, width=25, font=self.font)
        self.salary = Entry(self.add_window, width=25, font=self.font)

        self.name.place(x=180, y=5)
        self.phone.place(x=180, y=35)
        self.email.place(x=180, y=65)
        self.salary.place(x=180, y=95)

        Button(self.add_window, font=self.font, text="Добавить", activebackground="#f5f5dc", command=self.add_user).pack(side=BOTTOM, fill=X)

    def add_user(self):
        if len(self.name.get()) == 0 or len(self.phone.get()) == 0 or len(self.email.get()) == 0 or len(self.salary.get()) == 0:
            messagebox.showerror(title="Ошибка добавления", message="Не все поля заполнены!")
            self.add_window.focus()
        else:
            self.db_ex.insert_employee(name=self.name.get(), phone=self.phone.get(), email=self.email.get(), salary=self.salary.get())
            self.mainwindow_ex.update()