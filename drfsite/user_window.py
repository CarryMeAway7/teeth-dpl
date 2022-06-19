from tkinter import *
from tkinter import messagebox

new_window_5 = Tk()

def exit_program():
    info_str1=f'Завершение работы программы'
    messagebox.showinfo(title='Уведомление', message=info_str1)
    exit()

def kon():
    import Konysnost

new_window_5.title('EndoSys')
new_window_5.wm_attributes('-alpha', 0.9)
new_window_5.resizable(width=False, height=False)
canvas_1 = Canvas(new_window_5, height=300, width=600 )
canvas_1.pack()
frame3 = Frame(new_window_5)
frame3.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
title = Label(frame3, text='User Panel', font=10)
title.pack()
btn4 = Button(frame3, text='Подсчет коэффициента конусности/Код инструмента', command=kon)
btn4.pack()
btn1 = Button(frame3, text='Завершить работу', command=exit_program)
btn1.pack()
new_window_5.mainloop()