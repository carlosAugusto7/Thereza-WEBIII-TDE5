from tkinter import *

def manipular_lista():
    try:
        numeros = [int(entry_num1.get()), int(entry_num2.get()), int(entry_num3.get()), int(entry_num4.get())]
        
        contagem_9 = numeros.count(9)
        if 3 in numeros:
            posicao_3 = numeros.index(3)
        else:
            posicao_3 = -1
        pares = [num for num in numeros if num % 2 == 0]
        
        resultado.config(text=f"Quantas vezes o número 9 aparece: {contagem_9}\n"
                             f"Posição do primeiro número 3: {posicao_3}\n"
                             f"Números pares: {pares}")
    except ValueError:
        resultado.config(text="Por favor, insira números válidos!")

i = Tk()
i.title('Manipular Lista de Números')
i.geometry('400x300')
i['bg'] = '#CECECE'

label_instrucoes = Label(i, text="Insira 4 números:", font='Arial 12', bg='#CECECE')
label_instrucoes.pack(pady=10)

label_num1 = Label(i, text="Número 1:", font='Arial 10', bg='#CECECE')
label_num1.pack(pady=5)

entry_num1 = Entry(i, font='Arial 12')
entry_num1.pack(pady=5)

label_num2 = Label(i, text="Número 2:", font='Arial 10', bg='#CECECE')
label_num2.pack(pady=5)

entry_num2 = Entry(i, font='Arial 12')
entry_num2.pack(pady=5)

label_num3 = Label(i, text="Número 3:", font='Arial 10', bg='#CECECE')
label_num3.pack(pady=5)

entry_num3 = Entry(i, font='Arial 12')
entry_num3.pack(pady=5)

label_num4 = Label(i, text="Número 4:", font='Arial 10', bg='#CECECE')
label_num4.pack(pady=5)

entry_num4 = Entry(i, font='Arial 12')
entry_num4.pack(pady=5)

btn_processar = Button(i, text='Processar', font='Arial 12 bold', command=manipular_lista)
btn_processar.pack(pady=10)

resultado = Label(i, text="", font='Arial 12', bg='#CECECE')
resultado.pack(pady=20)

i.mainloop()
