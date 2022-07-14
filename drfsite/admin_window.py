import requests
import json

from tkinter import *
from tkinter import messagebox

new_window_1 = Tk()

def pac_history():
    a = requests.get('http://127.0.0.1:8000/api/v1/endo/')
    a.json()
    p = a.json()
    info_str = p
    json.dumps(p, indent=4)
    new_window_1.withdraw()
    messagebox.showinfo(title='Информация', message=info_str)

def exit_program():
    info_str1=f'Завершение работы программы'
    messagebox.showinfo(title='Уведомление', message=info_str1)
    exit()

def add_new_user2():
    import new_user

def edit_user():
    import edit_user

def kon():
    import Konysnost

def access():
    import access_rules

new_window_1.title('EndoSys')
new_window_1.wm_attributes('-alpha', 0.9)
new_window_1.resizable(width=False, height=False)

canvas_1 = Canvas(new_window_1, height=300, width=600 )
canvas_1.pack()

frame1 = Frame(new_window_1)
frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

title = Label(frame1, text='Admin Panel', font=10)
title.pack()

btn2 = Button(frame1, text='Создать нового пользователя', command=add_new_user2)
btn2.pack()
btn3 = Button(frame1, text='Редактировать существующего пользователя', command=edit_user)
btn3.pack()
btn4 = Button(frame1, text='Подсчет коэффициента конусности/Код инструмента', command=kon)
btn4.pack()
btn5 = Button(frame1, text='Права администратора', command=access)
btn5.pack()
btn6 = Button(frame1, text='История пациентов', command=pac_history)
btn6.pack()
btn1 = Button(frame1, text='Завершить работу', command=exit_program, )
btn1.pack()

new_window_1.mainloop()