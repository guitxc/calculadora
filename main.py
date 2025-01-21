import tkinter as tk
from tkinter import messagebox



def calcular():
    num1_text = entr_num1.get()
    num2_text = entr_num2.get()
    operacao = entr_oper.get()

    try:
        num1 = float(num1_text)
    except ValueError:
        messagebox.showerror('Erro', 'O 1° numero é invalido')
        return
    
    try:
        num2 = float(num2_text)
    except ValueError:
        messagebox.showerror('Erro', 'O 2° numero é invalido')
        return

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
            if num2 == 0:
                messagebox.showerror("Erro", "Divisão por zero não é permitida.")
                return
            resultado = num1 / num2
    elif operacao == "**":
        resultado = num1 ** num2
    else:
        messagebox.showerror("Erro", "Operação inválida. Use +, -, *, / ou **.")
        return
    
    resultado_label.config(text=f"Resultado: {num1} {operacao} {num2} = {resultado}")

janela = tk.Tk()
janela.title('Calculadora')
janela.geometry("300x200")
janela.minsize(300,200)
janela.maxsize(300,200)

tk.Label(janela,text='Coloque o 1° numero:').grid(row=0, column=0, padx=10, pady=5,sticky='e')
entr_num1 = tk.Entry(janela)
entr_num1.grid(row=0, column=1, padx=10, pady=5,sticky='e')

tk.Label(janela, text='Coloque a operação(+, -, *, /, **):').grid(row=1, column=0, padx=10, pady=5,sticky='e')
entr_oper = tk.Entry(janela)
entr_oper.grid(row=1, column=1, padx=10, pady=5,sticky='e')

tk.Label(janela,text='Coloque o 2° numero:').grid(row=2, column=0, padx=10, pady=5,sticky='e')
entr_num2 = tk.Entry(janela)
entr_num2.grid(row=2, column=1, padx=10, pady=5,sticky='e')

botao = tk.Button(janela, text='Calcular',command=calcular)
botao.grid(row=3, column=0 ,columnspan=2, pady=10)

resultado_label = tk.Label(janela, text='Seu resultado é:', font=('Arial', 12))
resultado_label.grid(row=5, column=0, columnspan=2,pady=10)
janela.columnconfigure(1,weight=1)

janela.mainloop()