from tkinter import *

def verificar_maior_que_limite():
    try:
        lista = list(map(int, entry_lista.get().split(',')))
        limite = int(entry_limite.get())
        
        for i, numero in enumerate(lista):
            if numero > limite:
                resultado.config(text=f"Índice do primeiro número maior que o limite: {i}")
                return
        
        resultado.config(text="Nenhum número é maior que o limite.")
    
    except ValueError:
        resultado.config(text="Por favor, insira números válidos!")

i = Tk()
i.title('Verificar Elementos Maiores que o Limite')
i.geometry('400x250')
i['bg'] = '#CECECE'

label_instrucoes = Label(i, text="Insira uma lista de números ordenados (separados por vírgula):", font='Arial 10', bg='#CECECE')
label_instrucoes.pack(pady=10)

entry_lista = Entry(i, font='Arial 12')
entry_lista.pack(pady=10)

label_limite = Label(i, text="Insira o limite desejado:", font='Arial 10', bg='#CECECE')
label_limite.pack(pady=10)

entry_limite = Entry(i, font='Arial 12')
entry_limite.pack(pady=10)

btn_verificar = Button(i, text='Verificar', font='Arial 12 bold', command=verificar_maior_que_limite)
btn_verificar.pack(pady=10)

resultado = Label(i, text="", font='Arial 12', bg='#CECECE')
resultado.pack(pady=20)

i.mainloop()
