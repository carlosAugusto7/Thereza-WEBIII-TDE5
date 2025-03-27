from tkinter import *

def verificar_numero():
    try:
        numero = float(entry_numero.get())
        if numero > 0:
            resultado.config(text="O número é positivo!")
        elif numero < 0:
            resultado.config(text="O número é negativo!")
        else:
            resultado.config(text="O número é zero!")
    except ValueError:
        resultado.config(text="Por favor, insira um número válido!")

i = Tk()
i.title('Verificador de Número')
i.geometry('400x200')
i['bg'] = '#CECECE'

label_instrucoes = Label(i, text="Insira um número para verificar se é positivo ou negativo:", font='Arial 12', bg='#CECECE')
label_instrucoes.pack(pady=10)

entry_numero = Entry(i, font='Arial 12')
entry_numero.pack(pady=10)

btn_verificar = Button(i, text='Verificar', font='Arial 12 bold', command=verificar_numero)
btn_verificar.pack(pady=10)

resultado = Label(i, text="", font='Arial 12', bg='#CECECE')
resultado.pack(pady=20)

i.mainloop()
