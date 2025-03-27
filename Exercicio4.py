from tkinter import *

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2
        if num2 != 0:
            divisao = num1 / num2
        else:
            divisao = "Não pode dividir por zero"
        
        resultado.config(text=f"Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}")
    except ValueError:
        resultado.config(text="Por favor, insira números válidos!")

i = Tk()
i.title('Calculadora Básica')
i.geometry('400x300')
i['bg'] = '#CECECE'

label_instrucoes = Label(i, text="Insira dois números para realizar as operações:", font='Arial 12', bg='#CECECE')
label_instrucoes.pack(pady=10)

label_num1 = Label(i, text="Número 1:", font='Arial 10', bg='#CECECE')
label_num1.pack(pady=5)

entry_num1 = Entry(i, font='Arial 12')
entry_num1.pack(pady=5)

label_num2 = Label(i, text="Número 2:", font='Arial 10', bg='#CECECE')
label_num2.pack(pady=5)

entry_num2 = Entry(i, font='Arial 12')
entry_num2.pack(pady=5)

btn_calcular = Button(i, text='Calcular', font='Arial 12 bold', command=calcular)
btn_calcular.pack(pady=10)

resultado = Label(i, text="", font='Arial 12', bg='#CECECE')
resultado.pack(pady=20)

i.mainloop()
