import math
import requests
from tkinter import *
import tkinter as tk

new_window_4 = Tk()

def distance_2_points():
    xPoint1 = textField1.get()
    xPoint1 = int(xPoint1)
    yPoint1 = textField2.get()
    yPoint1 = int(yPoint1)
    xPoint2 = textField3.get()
    xPoint2 = int(xPoint2)
    yPoint2 = textField4.get()
    yPoint2 = int(yPoint2)
    xPoint4 = textField5.get()
    xPoint4 = int(xPoint4)
    yPoint4 = textField6.get()
    yPoint4 = int(yPoint4)
    xPoint5 = textField7.get()
    xPoint5 = int(xPoint5)
    yPoint5 = textField8.get()
    yPoint5 = int(yPoint5)
    name = textField9.get()
    surname = textField10.get()
    xpoint10 = textField13.get()
    xpoint10 = int(xpoint10)
    ypoint10 = textField14.get()
    ypoint10 = int(ypoint10)

    distance_p2p3 = math.fabs(yPoint1-yPoint2) #наименьший катет
    distance_p1p3 = math.fabs(xPoint1-xPoint2) #наибольший катет
    distance_p1p2 = math.sqrt(distance_p1p3**2 + distance_p2p3**2) #гипотенуза - наибольший диаметр
    print('(В) Диаметр:', distance_p1p2)
    distance_p4p6 = math.fabs(yPoint4 - yPoint5) #наименьший катет
    distance_p5p6 = math.fabs(xPoint4 - xPoint5) #наибольший катет
    distance_p4p5 = math.sqrt(distance_p4p6 ** 2 + distance_p5p6 ** 2) #гипотенуза - наименьший диаметр
    print('(Н) Диаметр:', distance_p4p5)

    x_p6 = math.fabs(xPoint1+(distance_p1p3/2))
    y_p6 = math.fabs(yPoint2+(distance_p2p3/2))
    x_p7 = math.fabs(xPoint4+(distance_p4p6/2))
    y_p7 = math.fabs(yPoint5+(distance_p5p6/2))

    distance_p6p8 = math.fabs(y_p7 - y_p6)
    distance_p8p7 = math.fabs(x_p7 - x_p6)
    #distance_p6p7 = math.sqrt(distance_p8p7**2 + distance_p6p8**2)

    x_p9 = math.fabs(x_p6+(distance_p8p7/2))
    y_p9 = math.fabs(y_p7+(distance_p6p8/2))

    distance_p10p11 = math.fabs(ypoint10 - y_p9)
    distance_p9p11 = math.fabs(x_p9 - xpoint10)
    distance_p9p10 = math.sqrt(distance_p10p11**2 + distance_p9p11**2)

    if xPoint1>xPoint2:
        Vxmid_p1p2 = (distance_p1p3/2) + xPoint2
        print("x1:", Vxmid_p1p2)
    else:
        Vxmid_p1p2 = (distance_p1p3 / 2) + xPoint1
        print("x1:", Vxmid_p1p2)
    if yPoint1>yPoint2:
        Vymid_p1p2 = (distance_p2p3/2) + yPoint2
        print("y1:", Vymid_p1p2)
    else:
        Vymid_p1p2 = (distance_p2p3 / 2) + yPoint1
        print("y1:", Vymid_p1p2)
    if xPoint4>xPoint5:
        Nxmid_p1p2 = (distance_p5p6/2) + xPoint5
        print("x2:", Nxmid_p1p2)
    else:
        Nxmid_p1p2 = (distance_p5p6 / 2) + xPoint4
        print("x2:", Nxmid_p1p2)
    if yPoint4>yPoint5:
        Nymid_p1p2 = (distance_p4p6/2) + yPoint5
        print("y2:", Nymid_p1p2)

    l_dis_p2p3 = math.fabs(Vymid_p1p2-Nymid_p1p2)
    l_dis_p1p3 = math.fabs(Vxmid_p1p2-Nxmid_p1p2)
    l = math.sqrt(l_dis_p2p3**2 + l_dis_p1p3**2)
    kon = (distance_p1p2-distance_p4p5)/l
    if kon <= 0.06:
        label5['text'] = "Цветовой код инстурмента: Розовый /номер размера по ст. ISO:", kon
        cat = 1
    if kon <= 0.08 and kon > 0.06:
        label5['text'] = "Цветовой код инстурмента: Серый /номер размера по ст. ISO:", kon
        cat = 2
    if kon <= 0.1 and kon > 0.08:
        label5['text'] = "Цветовой код инстурмента: Фиолетовый /номер размера по ст. ISO:", kon
        cat = 3
    if (kon <= 0.15 and kon > 0.1) or (kon > 40 and kon <= 45) or (kon > 80 and kon <=90):
        label5['text'] = "Цветовой код инстурмента: Белый /номер размера по ст. ISO:", kon
        cat = 4
    if (kon <= 0.20 and kon > 0.15) or (kon > 45 and kon <= 50) or (kon > 90 and kon <=100):
        label5['text'] = "Цветовой код инстурмента: Желтый /номер размера по ст. ISO:", kon
        cat = 5
    if (kon <= 0.25 and kon > 0.20) or (kon > 50 and kon <= 55) or (kon > 100 and kon <=110):
        label5['text'] = "Цветовой код инстурмента: Красный /номер размера по ст. ISO:", kon
        cat = 6
    if (kon <= 0.30 and kon > 0.25) or (kon > 55 and kon <= 60) or (kon > 110 and kon <=120):
        label5['text'] = "Цветовой код инстурмента: Синий /номер размера по ст. ISO:", kon
        cat = 7
    if (kon <= 0.35 and kon > 0.30) or (kon > 65 and kon <= 70) or (kon > 120 and kon <=130):
        label5['text'] = "Цветовой код инстурмента: Зеленый /номер размера по ст. ISO:", kon
        cat = 8
    if (kon <= 0.40 and kon > 0.35) or (kon > 75 and kon <= 80) or (kon > 130 and kon <=140):
        label5['text'] = "Цветовой код инстурмента: Черный /номер размера по ст. ISO:", kon
        cat = 9
    print("Длина конуса:", l)
    print("Коэффициент конусности:", kon)
    label1['text'] = "(В) Диаметр:", distance_p1p2
    label2['text'] = "(Н) Диаметр:", distance_p4p5
    label3['text'] = "Длинна конуса без учета кривизны:", l
    label4['text'] = "Коэффициент конусности:", kon
    label16['text'] = "Отклонение:", distance_p9p10
    login = textField11.get()
    password = textField12.get()

    data = {
        'username': login,
        'password': password,
    }

    a = requests.post('http://127.0.0.1:8000/auth/token/login/', json=data)
    a.json()
    data = {
        'name': name,
        'surname': surname,
        'cat': cat
    }

    b = requests.post('http://127.0.0.1:8000/api/v1/endo/',
                      headers={'Authorization': f'Token {a.json()["auth_token"]}'},
                      json=data)
    b.json()

new_window_4.title('EndoSys')
new_window_4.wm_attributes('-alpha', 0.9)
new_window_4.geometry('1320x360')
new_window_4.resizable(width=False, height=False)
canvas_1 = Canvas(new_window_4, height=300, width=900 )
canvas_1.pack()
frame4 = Frame(new_window_4)
frame4.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
title = Label(frame4, text='Подсчет конусности', font=10)
title.pack()
btn2 = Button(frame4, text='Ввести данные', command=distance_2_points)
btn2.pack()
textField1 = Entry(frame4, bg='white')
textField1.pack()
textField2 = Entry(frame4, bg='white')
textField2.pack()
textField3 = Entry(frame4, bg='white')
textField3.pack()
textField4 = Entry(frame4, bg='white')
textField4.pack()
textField5 = Entry(frame4, bg='white')
textField5.pack()
textField6 = Entry(frame4, bg='white')
textField6.pack()
textField7 = Entry(frame4, bg='white')
textField7.pack()
textField8 = Entry(frame4, bg='white')
textField8.pack()
textField9 = Entry(frame4, bg='white')
textField9.pack()
textField10 = Entry(frame4, bg='white')
textField10.pack()
textField11 = Entry(frame4, bg='white')
textField11.pack()
textField12 = Entry(frame4, bg='white', show='#')
textField12.pack()
textField13 = Entry(frame4, bg='white')
textField13.pack()
textField14 = Entry(frame4, bg='white')
textField14.pack()

label1 = tk.Label(new_window_4)
label1.place(x=35,y=35)
label2 = tk.Label(new_window_4)
label2.place(x=35,y=60)
label3 = tk.Label(new_window_4)
label3.place(x=35,y=85)
label4 = tk.Label(new_window_4)
label4.place(x=35,y=110)
label5 = tk.Label(new_window_4)
label5.place(x=35,y=135)
label16 = tk.Label(new_window_4)
label16.place(x=35,y=160)

poetry = "x1(в):\n"
label6 = Label(frame4, text=poetry, justify=CENTER)
label6.place(relx=.42, rely=.165)
poetry = "y1(в):\n"
label7 = Label(frame4, text=poetry, justify=CENTER)
label7.place(relx=.42, rely=.23)
poetry = "x2(в):\n"
label8 = Label(frame4, text=poetry, justify=CENTER)
label8.place(relx=.42, rely=.295)
poetry = "y2(в):\n"
label9 = Label(frame4, text=poetry, justify=CENTER)
label9.place(relx=.42, rely=.36)
poetry = "x1(н):\n"
label10 = Label(frame4, text=poetry, justify=CENTER)
label10.place(relx=.42, rely=.42)
poetry = "y1(н):\n"
label11 = Label(frame4, text=poetry, justify=CENTER)
label11.place(relx=.42, rely=.48)
poetry = "x2(н):\n"
label12 = Label(frame4, text=poetry, justify=CENTER)
label12.place(relx=.42, rely=.543)
poetry = "y2(н):\n"
label13 = Label(frame4, text=poetry, justify=CENTER)
label13.place(relx=.42, rely=.605)
poetry = "Name:\n"
label14 = Label(frame4, text=poetry, justify=CENTER)
label14.place(relx=.42, rely=.680)
poetry = "Surname:\n"
label15 = Label(frame4, text=poetry, justify=CENTER)
label15.place(relx=.408, rely=.745)
poetry = "staff login:\n"
label14 = Label(frame4, text=poetry, justify=CENTER)
label14.place(relx=.403, rely=.814)
poetry = "staff pass:\n"
label15 = Label(frame4, text=poetry, justify=CENTER)
label15.place(relx=.4055, rely=.880)
new_window_4.mainloop()


# import requests
# a = requests.post('http://127.0.0.1:8000/auth/token/login/', data={'username':'root','password':'1234'})
# a.json()
# {'auth_token': 'e89d7eb4eef9a28136124a9a4cd1d206ab717f52'}
# b = requests.post('http://127.0.0.1:8000/api/v1/endo/', headers={'Authorization':f'Token {a.json()["auth_token"]}'})
# b.json()
# {'name': ['Обязательное поле.']}
# b = requests.post('http://127.0.0.1:8000/api/v1/endo/', headers={'Authorization':f'Token {a.json()["auth_token"]}'}, data={'name':'anton', 'surname':'antonov','cat':3})
# b.json()
# {'name': 'aaa', 'cat_id': None}
# python requests
