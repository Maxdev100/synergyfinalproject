from tkinter import ttk
from classes.db import *
from classes.add_window import *


class MainWindow:
    def __init__(self):
        # Создание окна
        self.toolbar = None
        self.app = Tk()
        self.app.title("Список сотрудников компании")
        self.app.geometry("850x500")
        self.app.resizable(False, False)
        self.app.protocol("WM_DESTROY_WINDOW", exit)

        # Инициализация всех виджетов
        self.init_widgets()

        # Обновление таблицы с сотрудниками
        self.update()

        # Цикл приложения
        self.app.mainloop()

    def init_widgets(self):
        # Тулбар с кнопками
        self.toolbar = Frame(self.app)
        self.toolbar.pack()

        # Изображения кнопок
        self.add_btn_image = PhotoImage(file="./img/add.png")
        self.edit_btn_image = PhotoImage(file="./img/edit.png")
        self.update_btn_image = PhotoImage(file="./img/update.png")
        self.search_btn_image = PhotoImage(file="./img/search.png")
        self.delete_btn_image = PhotoImage(file="./img/delete.png")

        # Кнопка добавления
        add_btn = Button(self.toolbar, image=self.add_btn_image, command=lambda: AddWindow(db, self))
        add_btn.pack(side=LEFT, pady=2, padx=17)

        # Кнопка изменения
        edit_btn = Button(self.toolbar, image=self.edit_btn_image)
        edit_btn.pack(side=LEFT, pady=2, padx=17)

        # Кнопка обновления
        delete_btn = Button(self.toolbar, image=self.delete_btn_image)
        delete_btn.pack(side=LEFT, pady=2, padx=17)

        # Кнопка удаления
        update_btn = Button(self.toolbar, image=self.update_btn_image, command=self.update)
        update_btn.pack(side=LEFT, pady=2, padx=17)

        # Кнопка поиска
        search_btn = Button(self.toolbar, image=self.search_btn_image)
        search_btn.pack(side=LEFT, pady=2, padx=17)

        # Таблица
        columns = ("#1", "#2", "#3", "#4")
        self.treeview = ttk.Treeview(self.app, show="headings", columns=columns)
        self.treeview.heading("#1", text="ФИО")
        self.treeview.heading("#2", text="Номер телефона")
        self.treeview.heading("#3", text="Электронная почта")
        self.treeview.heading("#4", text="Заработная плата")

        # Скроллбар таблицы
        self.treeview_yscroll = Scrollbar(self.app, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.treeview_yscroll.set)
        self.treeview_yscroll.pack(side=RIGHT, fill=Y)

        # Упаковка таблицы
        self.treeview.pack(fill=BOTH, expand=True)

    # Обновляет список пользователей
    def update(self):
        data = db.select_all()
        self.treeview.delete(*self.treeview.get_children())
        for employee in data:
            self.treeview.insert("", END, values=employee)

    # Выход из программы
    def exit(self):
        db.close_connection()
        self.app.destroy()


# Старт программы
if __name__ == "__main__":
    db = DB()  # Создание БД
    main_window = MainWindow()
