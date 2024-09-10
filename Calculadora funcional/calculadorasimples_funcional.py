import tkinter as tk

# Esta é uma calculadora simples e funcional criada utilizando interface gráfica do tkinter.

class Calculadora:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Calculadora Simples')
        self.janela.geometry('300x500')
        self.janela.configure(background='black')

        self.equacao = ""
        self.display = tk.Entry(master, justify='right', font=('Arial', 18), bd=10, insertwidth=2, background='black', foreground='white')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        self.btn7 = tk.Button(master, text='7', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('7'))
        self.btn7.grid(row=1, column=0, sticky='nsew')

        self.btn8 = tk.Button(master, text='8', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('8'))
        self.btn8.grid(row=1, column=1, sticky='nsew')

        self.btn9 = tk.Button(master, text='9', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('9'))
        self.btn9.grid(row=1, column=2, sticky='nsew')

        self.btn_add = tk.Button(master, text='+', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('+'))
        self.btn_add.grid(row=1, column=3, sticky='nsew')

        self.btn6 = tk.Button(master, text='6', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('6'))
        self.btn6.grid(row=2, column=0, sticky='nsew')

        self.btn5 = tk.Button(master, text='5', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('5'))
        self.btn5.grid(row=2, column=1, sticky='nsew')

        self.btn4 = tk.Button(master, text='4', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('4'))
        self.btn4.grid(row=2, column=2, sticky='nsew')

        self.btn_subtrair = tk.Button(master, text='-', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('-'))
        self.btn_subtrair.grid(row=2, column=3, sticky='nsew')

        self.btn1 = tk.Button(master, text='1', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('1'))
        self.btn1.grid(row=3, column=0, sticky='nsew')

        self.btn2 = tk.Button(master, text='2', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('2'))
        self.btn2.grid(row=3, column=1, sticky='nsew')

        self.btn3 = tk.Button(master, text='3', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('3'))
        self.btn3.grid(row=3, column=2, sticky='nsew')

        self.btn_mult = tk.Button(master, text='*', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('*'))
        self.btn_mult.grid(row=3, column=3, sticky='nsew')

        self.btn0 = tk.Button(master, text='0', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('0'))
        self.btn0.grid(row=4, column=0, sticky='nsew')

        self.btn_ponto = tk.Button(master, text='.', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('.'))
        self.btn_ponto.grid(row=4, column=1, sticky='nsew')

        self.btn_clear = tk.Button(master, text='C', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=self.limpar)
        self.btn_clear.grid(row=4, column=2, sticky='nsew')

        self.btn_divide = tk.Button(master, text='/', padx=20, pady=20, font=('Arial', 18), background='black', foreground='white', command=lambda: self.clicar('/'))
        self.btn_divide.grid(row=4, column=3, sticky='nsew')

        self.btn_equal = tk.Button(master, text='=', padx=20, pady=20, font=('Arial', 18), background='green', command=self.calcular)
        self.btn_equal.grid(row=5, column=0, columnspan=4, sticky='nsew')

        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def clicar(self, char):
        self.equacao += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.equacao)

    def limpar(self):
        self.equacao = ""
        self.display.delete(0, tk.END)

    def calcular(self):
        try:
            resultado = str(eval(self.equacao))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, resultado)
            self.equacao = resultado
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro")
            self.equacao = ""

janela = tk.Tk()
app = Calculadora(janela)
janela.mainloop()
