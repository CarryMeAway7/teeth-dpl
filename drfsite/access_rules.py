from tkinter import *
import sqlite3

from tkinter import messagebox
import os
import hashlib

new_window_3 = Tk()

def update_sqlite_table(login, access):
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = f"Update auth_user set is_superuser = '{access}' where username = '{login}'"
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def btn_click_create():
    login = loginInput1.get()
    access = textField1.get()

    if access == '1' or access == '0':
        update_sqlite_table(login, access)
        info_str1 = f'Редактирование успешно завершено'
        messagebox.showinfo(title='Уведомление', message=info_str1)
        new_window_3.destroy()
    else:
        info_str1 = f'Введено неверное значение AdminRules'
        messagebox.showinfo(title='Уведомление', message=info_str1)

    # f = open("C:/Users/Study/PycharmProjects/pyqt/users/"+login+"_access", 'w')
    # f.write(access)
    # f.close()

new_window_3['bg'] = '#fafafa'
new_window_3.title('EndoSys')
new_window_3.wm_attributes('-alpha', 0.9)
new_window_3.resizable(width=False, height=False)
canvas_2 = Canvas(new_window_3, height=200, width=400)
canvas_2.pack()
frame2 = Frame(new_window_3)
frame2.place(relx = 0.01, rely=0.01, relwidth=0.98, relheight=0.98)
title = Label(new_window_3, text='Edit access', font=10)
title.pack()
loginInput1 = Entry(frame2, bg='white')
loginInput1.pack()
textField1 = Entry(frame2, bg='white')
textField1.pack()
btn_back = Button(frame2, text='Изменить', command=btn_click_create)
btn_back.pack()

poetry = "Логин:\n"
label1 = Label(frame2, text=poetry, justify=CENTER)
label1.place(relx=.23, rely=.009)

poetry = "Access:\n"
label2 = Label(frame2, text=poetry, justify=CENTER)
label2.place(relx=.225, rely=.1)

new_window_3.mainloop()