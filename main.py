from tkinter import *
from tkinter import messagebox

root = Tk()


def btn_click(): 
    ves = float(vesInput.get())
    rost = float(rostInput.get())
    years = float(yearsInput.get()) 
    itog = 10*ves+6.25*rost-5*years

    info_str =f'Данные: {str(itog)}'
    messagebox.showinfo(title='Кол-во каллорий в день: ', message=info_str,)

root['bg']='#fca1a1'
root.title('Yes')
root.geometry('500x350')

canvas=Canvas(root, height=500, width=350)
canvas.pack()

frame = Frame(root, bg='#fca1a1')
frame.place(relwidth=1, relheight=1)

#Текст ввода
title = Label(frame, text='Введите свои данные!!!')
title.pack(pady=10)

#Вес
title = Label(frame, text='Ваш вес:')
title.pack(pady=5)

vesInput = Entry(frame, bg='white')
vesInput.pack(pady=3)

#Рост
title = Label(frame, text='Ваш рост:')
title.pack(pady=5)

rostInput = Entry(frame, bg='white')
rostInput.pack(pady=3)

#Возраст
title = Label(frame, text='Ваш возраст:')
title.pack(pady=5)

yearsInput = Entry(frame, bg='white')
yearsInput.pack(pady=3)



btn = Button(frame, text='Вычеслить кол-во каллорий в день', bg='#c1bf44', command=btn_click)
btn.pack(pady=12)




root.mainloop()