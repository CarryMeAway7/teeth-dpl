import requests
import sqlite3
import os
import hashlib

from tkinter import *
from tkinter import messagebox

new_window_3 = Tk()

def delete_record(login_old):
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_delete_query = f"DELETE from auth_user where username = '{login_old}'"
        cursor.execute(sql_delete_query)
        sqlite_connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def btn_click_create():
    login_old = loginInput1.get()
    login_new = loginInput2.get()
    password_new = textField1.get()
    email = login_new + '@mail.ru'

    data = {
        'username': login_new,
        'password': password_new,
        'email': email
    }

    a = requests.post('http://127.0.0.1:8000/api/v1/authusers/', json=data)
    a.json()

    delete_record(login_old)

    info_str1 = f'Редактирование успешно завершено'
    messagebox.showinfo(title='Уведомление', message=info_str1)

new_window_3['bg'] = '#fafafa'
new_window_3.title('EndoSys')
new_window_3.wm_attributes('-alpha', 0.9)
new_window_3.resizable(width=False, height=False)

canvas_2 = Canvas(new_window_3, height=200, width=400)
canvas_2.pack()

frame5 = Frame(new_window_3)
frame5.place(relx = 0.01, rely=0.01, relwidth=0.98, relheight=0.98)

title = Label(new_window_3, text='Edit User', font=10)
title.pack()

loginInput1 = Entry(frame5, bg='white')
loginInput1.pack()
loginInput2 = Entry(frame5, bg='white')
loginInput2.pack()

textField1 = Entry(frame5, bg='white')
textField1.pack()

btn_back = Button(frame5, text='Изменить', command=btn_click_create)
btn_back.pack()

poetry = "Логин(старый):\n"
label1 = Label(frame5, text=poetry, justify=CENTER)
label1.place(relx=.11, rely=.0)

poetry = "Логин(новый):\n"
label2 = Label(frame5, text=poetry, justify=CENTER)
label2.place(relx=.12, rely=.086)

poetry = "Пароль(новый):\n"
label3 = Label(frame5, text=poetry, justify=CENTER)
label3.place(relx=.1, rely=.17)

new_window_3.mainloop()