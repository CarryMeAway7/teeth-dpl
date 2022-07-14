import requests
import sqlite3
import hashlib
import tkinter.ttk as ttk

from tkinter import *
from tkinter import messagebox

new_window_2 = Tk()

def update_sqlite_table(login_new):
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_update_query = f"Update auth_user set is_superuser = 1 where username = '{login_new}'"
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
    login_new = loginInput1.get()
    password_new = passField1.get()
    email = login_new + '@mail.ru'
    access = textfield1.get()

    data = {
        'username': login_new,
        'password': password_new,
        'email': email
    }

    a = requests.post('http://127.0.0.1:8000/api/v1/authusers/', json=data)
    a.json()
    if access == '1':
        update_sqlite_table(login_new)

    info_str1 = f'Создание успешно завершено'
    messagebox.showinfo(title='Уведомление', message=info_str1)

new_window_2['bg'] = '#fafafa'
new_window_2.title('EndoSys')
new_window_2.wm_attributes('-alpha', 0.9)

canvas_2 = Canvas(new_window_2, height=200, width=300)
canvas_2.pack()

frame6 = Frame(new_window_2)
frame6.place(relx = 0.01, rely=0.01, relwidth=0.98, relheight=0.98)

title = Label(new_window_2, text='Add New User', font=10)
title.pack()

loginInput1 = Entry(frame6, bg='white')
loginInput1.pack()

passField1 = Entry(frame6, bg='white')
passField1.pack()

textfield1 = Entry(frame6, bg='white')
textfield1.pack()

btn_back = Button(frame6, text='Создать', command=btn_click_create)
btn_back.pack()

poetry1 = "Логин:\n"
label10 = Label(frame6, text=poetry1, justify=CENTER)
label10.place(relx=.125, rely=.0)

poetry2 = "Пароль:\n"
label12 = Label(frame6, text=poetry2, justify=CENTER)
label12.place(relx=.1, rely=.086)

poetry3 = "Access:\n"
label13 = Label(frame6, text=poetry3, justify=CENTER)
label13.place(relx=.116, rely=.17)

new_window_2.mainloop()
