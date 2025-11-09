from tkinter import *

window = Tk()
window.title("Калькулятор")
window.geometry('350x400')

entry = Entry(window, width=15, font=('', 20))
entry.place(x = 100, y = 50)

def input_into_entry(symbol):
    entry.insert(END, symbol)

def clear():
    entry.delete(0, END)

def count_result():
    text = entry.get()
    result = 0
    if '+' in text:
        splitted_text = text.split('+')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first+second
    if '-' in text:
        splitted_text = text.split('-')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first-second
    if '/' in text:
        splitted_text = text.split('/')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        if second != 0:
            result = first/second
        else:
            result = 'error'
    if '*' in text:
        splitted_text = text.split('*')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first*second
    if result % 1 == 0:
        result = int(result)
    clear()
    entry.insert(0, result)

btn1 = Button(window, bg='black', fg='white', text='1', command=lambda : input_into_entry('1'))
btn1.place(x=100, y=100, width=50, height=50)

btn2 = Button(window, bg='black', fg='white', text='2', command=lambda : input_into_entry('2'))
btn2.place(x=160, y=100, width=50, height=50)

btn3 = Button(window, bg='black', fg='white', text='3', command=lambda : input_into_entry('3'))
btn3.place(x=220, y=100, width=50, height=50)

btn4 = Button(window, bg='black', fg='white', text='4', command=lambda : input_into_entry('4'))
btn4.place(x=100, y=160, width=50, height=50)

btn5 = Button(window, bg='black', fg='white', text='5', command=lambda : input_into_entry('5'))
btn5.place(x=160, y=160, width=50, height=50)

btn6 = Button(window, bg='black', fg='white', text='6', command=lambda : input_into_entry('6'))
btn6.place(x=220, y=160, width=50, height=50)

btn7 = Button(window, bg='black', fg='white', text='7', command=lambda : input_into_entry('7'))
btn7.place(x=100, y=220, width=50, height=50)

btn8 = Button(window, bg='black', fg='white', text='8', command=lambda : input_into_entry('8'))
btn8.place(x=160, y=220, width=50, height=50)

btn9 = Button(window, bg='black', fg='white', text='9', command=lambda : input_into_entry('9'))
btn9.place(x=220, y=220, width=50, height=50)

btn_zero = Button(window, bg='black', fg='white', text='0', command=lambda : input_into_entry('0'))
btn_zero.place (x=160, y=280, width=50, height=50)

btn_plus = Button(window, bg='black', fg='white', text='+', command=lambda : input_into_entry('+'))
btn_plus.place (x=280, y=100, width=50, height=50)

btn_minus = Button(window, bg='black', fg='white', text='-', command=lambda : input_into_entry('-'))
btn_minus.place (x=280, y=160, width=50, height=50)

btn_divide = Button(window, bg='black', fg='white', text='/', command=lambda : input_into_entry('/'))
btn_divide.place (x=280, y=220, width=50, height=50)

btn_multiply = Button(window, bg='black', fg='white', text='*', command=lambda : input_into_entry('*'))
btn_multiply.place (x=280, y=280, width=50, height=50)

btn_clear = Button(window, bg='black', fg='white', text='CE', command=clear)
btn_clear.place (x=280, y=340, width=50, height=50)

btn_dot = Button(window, bg='black', fg='white', text='.', command=lambda : input_into_entry('.'))
btn_dot.place (x=100, y=280, width=50, height=50)

btn_result = Button(window, bg='black', fg='white', text='=', command=count_result)
btn_result.place (x=220, y=280, width=50, height=50)

window.mainloop()