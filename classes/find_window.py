from tkinter import *


class SearchWindow:
    # Конструктор класса принимает объект главного окна и БД
    def __init__(self, db_ex, mainwindow_ex):
        self.mainwindow_ex = mainwindow_ex
        self.db_ex = db_ex
        self.font = "Arial 14"

        # Инициализация окна
        self.search_window = Toplevel()
        self.search_window.geometry("420x110")
        self.search_window.title("Искать сотрудника по имени")
        self.search_window.resizable(False, False)
        self.search_window.focus()
        self.search_window.bind("<Key>", self.check_empty)

        # Добавление текстового виджета Label с ФИО
        Label(self.search_window, font=self.font, text="ФИО").place(x=5, y=5)

        # Счетчик найденных людей
        self.founded_people = Label(self.search_window, font=self.font, text="Найдено людей: 0")
        self.founded_people.place(x=5, y=40)

        # Текстовое поле
        self.name = Entry(self.search_window, width=30, font=self.font)
        self.name.focus()
        self.name.place(x=65, y=5)

        # Кнопка поиска
        self.find_btn = Button(self.search_window, font=self.font, text="Искать", activebackground="#f5f5dc",
                               command=self.find, state=DISABLED)
        self.find_btn.pack(side=BOTTOM, fill=X)

        self.search_window.mainloop()

    # Функция поиска
    def find(self):
        name = self.name.get()
        self.mainwindow_ex.treeview.delete(*self.mainwindow_ex.treeview.get_children())
        if len(name) > 0:
            # Получение списка пользователей по имени
            users = self.db_ex.select_all(name=name, soft=True)
            self.founded_people.config(text=f"Найдено людей: {len(users)}")

            # Если результатов поиска > 0, перебор каждого пользователя и внесение в таблицу
            if len(users) > 0:
                for user in users:
                    self.mainwindow_ex.treeview.insert("", END, values=user)

    # Проверка, есть ли в текстовом поле текст. Если нет - заблокировать кнопку
    def check_empty(self, event):
        if len(self.name.get()) > 0:
            self.find_btn.config(state=NORMAL)
        else:
            self.find_btn.config(state=DISABLED)
