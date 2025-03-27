from tkinter import *

def verificar_bissexto():
    try:
        ano = int(entry_ano.get())
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            resultado.config(text="O ano é bissexto!")
        else:
            resultado.config(text="O ano não é bissexto!")
    except ValueError:
        resultado.config(text="Por favor, insira um ano válido!")

i = Tk()
i.title('Verificador de Ano Bissexto')
i.geometry('400x200')
i['bg'] = '#CECECE'

label_instrucoes = Label(i, text="Insira um ano para verificar se é bissexto:", font='Arial 12', bg='#CECECE')
label_instrucoes.pack(pady=10)

entry_ano = Entry(i, font='Arial 12')
entry_ano.pack(pady=10)

btn_verificar = Button(i, text='Verificar', font='Arial 12 bold', command=verificar_bissexto)
btn_verificar.pack(pady=10)

resultado = Label(i, text="", font='Arial 12', bg='#CECECE')
resultado.pack(pady=20)

i.mainloop()
