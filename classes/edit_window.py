from tkinter import *
from tkinter import messagebox


class EditWindow:
    # Конструктор класса принимает объект БД и объект главного окна
    def __init__(self, db_ex, mainwindow_ex):
        self.db_ex = db_ex
        self.mainwindow_ex = mainwindow_ex
        self.font = "Arial 14"

        # Инициализация окна
        self.edit_window = Toplevel()
        self.edit_window.geometry("470x220")
        self.edit_window.title("Редактировать сотрудника")
        self.edit_window.resizable(False, False)
        self.edit_window.focus()

        # Создание текстовых меток, кнопки и полей ввода
        Label(self.edit_window, text="ФИО", font=self.font).place(x=5, y=5)
        Label(self.edit_window, text="Телефон", font=self.font).place(x=5, y=35)
        Label(self.edit_window, text="Электронная почта", font=self.font).place(x=5, y=65)
        Label(self.edit_window, text="Зарплата", font=self.font).place(x=5, y=95)

        self.name = Entry(self.edit_window, width=25, font=self.font)
        self.phone = Entry(self.edit_window, width=25, font=self.font)
        self.email = Entry(self.edit_window, width=25, font=self.font)
        self.salary = Entry(self.edit_window, width=25, font=self.font)

        self.name.place(x=180, y=5)
        self.phone.place(x=180, y=35)
        self.email.place(x=180, y=65)
        self.salary.place(x=180, y=95)

        info = Label(self.edit_window, font=self.font, foreground="#333333",
                     text="Внимание! Изменить ФИО сотрудника можно\nтолько удалив текущего и добавив нового.")
        info.place(x=25, y=130)

        Button(self.edit_window, font=self.font, text="Применить изменения", activebackground="#f5f5dc",
               command=self.apply_changes).pack(side=BOTTOM, fill=X)

        # Заполнение полей ввода
        self.fill_fields()

    # Заполнение полей ввода данными. Поле "ФИО" заблокировано
    def fill_fields(self):
        # Получение ФИО выбранного сотрудника
        name = None
        try:
            name = self.mainwindow_ex.treeview.item(self.mainwindow_ex.treeview.selection()[0])["values"][0]

            # Получение данных по ФИО
            data = self.db_ex.select_all(name=name)

            # Вставка данных
            self.name.insert(0, data[0][0])
            self.name.config(state=DISABLED)

            self.phone.insert(0, data[0][1])
            self.email.insert(0, data[0][2])
            self.salary.insert(0, data[0][3])
        except:
            messagebox.showerror(title="Ошибка", message="Необходимо выбрать сотрудника!")
            self.edit_window.destroy()

    def apply_changes(self):
        self.db_ex.edit(name=self.name.get(), phone=self.phone.get(), email=self.email.get(), salary=self.salary.get())
        self.mainwindow_ex.update()
