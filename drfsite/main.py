import hashlib
import datetime
import platform
import bs4, requests
import sqlite3

from tkinter import *
from tkinter import messagebox

root = Tk()

def ad_win():
    import admin_window

def us_win():
    import user_window

def read_sqlite_table(records,login):
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from auth_user"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        name = []
        for row in records:
            print("ID:", row[0])
            print("Админ?:", row[3])
            print("Имя:", row[4], end="\n\n")
            if row[3] == 1:
                name.append(str(row[4]))

        print(name)

        if login in name:
            ad_win()
        else:
            us_win()

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def btn_click():

    login = loginInput.get()
    password = passField.get()

    data = {
        'username': login,
        'password': password,
    }

    a = requests.post('http://127.0.0.1:8000/auth/token/login/', json=data)
    a.json()

    if a.json() == {'non_field_errors': ['Невозможно войти с предоставленными учетными данными.']}:
        messagebox.showerror(title='Error', message='Невозможно войти с предоставленными учетными данными.')
    else:
        if 200 <= a.status_code <= 300:
            info_str = f'Вход выполнен успешно'
            root.withdraw()
            messagebox.showinfo(title='Уведомление', message=info_str)
            # info(login)
            read_sqlite_table(1,login)
        else:
            info_str = f'Произошла ошибка! Обратитесь к администратору'
            root.withdraw()
            messagebox.showinfo(title='Уведомление', message=info_str)
            us_win()

root['bg'] = '#fafafa'
root.title('EndoSys')
root.wm_attributes('-alpha', 0.85)
root.geometry('600x300')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=1600, width=900)

background_label = Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = Frame(root)
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

title = Label(text='Укажите логин и пароль от вашей учетной записи', font=10)
title.grid(row=0, column=5, padx=115, pady=5)

poetry = "Логин:\n"
label1 = Label(text=poetry, justify=CENTER)
label1.place(relx=.31, rely=.17)

loginInput = Entry(bg='white')
loginInput.grid(row=1, column=5, padx=115, pady=18)

passField = Entry(frame, bg='white', show='#')
passField.grid(row=1, column=0, padx=226, pady=75)

poetry = "Пароль:\n"
label2 = Label(text=poetry, justify=CENTER)
label2.place(relx=.296, rely=.26)

btn = Button(frame, text='Войти', command=btn_click)
btn.grid(row=2, column=0, padx=0, pady=0)

root.mainloop()
