import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Torre de Hanói')
        self.janela.geometry('800x400')
        
        self.discos = 5
        self.movimentos = 0
        self.selecionada = None

        self.torre_a = list(range(self.discos, 0, -1))
        self.torre_b = []
        self.torre_c = []

        self.cnv = tk.Canvas(self.janela, width=600, height=300, bg='white')
        self.cnv.pack(side=tk.LEFT, padx=10, pady=10)

        self.posicoes = [(100, 250), (300, 250), (500, 250)]

        self.lbl_movimentos = tk.Label(self.janela, text=f'Movimentos: {self.movimentos}')
        self.lbl_movimentos.pack(side=tk.TOP, padx=10, pady=10)

        self.frm = tk.Frame(self.janela)
        self.frm.pack(side=tk.RIGHT, padx=10, pady=10)

        self.btn_a = tk.Button(self.frm, text='Torre A', command=lambda: self.selecionar_torre('A'))
        self.btn_a.pack(pady=5)

        self.btn_b = tk.Button(self.frm, text='Torre B', command=lambda: self.selecionar_torre('B'))
        self.btn_b.pack(pady=5)

        self.btn_c = tk.Button(self.frm, text='Torre C', command=lambda: self.selecionar_torre('C'))
        self.btn_c.pack(pady=5)

        self.mostrar_torres()
        self.mostrar_discos()

    def mostrar_torres(self):
        for i in self.posicoes:
            self.cnv.create_line(i[0], 100, i[0], 250, width=5)

    def mostrar_discos(self):
        self.cnv.delete('disco')
        def desenhar_torre(torre, pos):
            for k, disco in enumerate(torre):
                largura = disco * 20
                x0 = pos[0] - largura // 2
                y0 = pos[1] - (k + 1) * 20
                x1 = pos[0] + largura // 2
                y1 = pos[1] - k * 20
                self.cnv.create_rectangle(x0, y0, x1, y1, fill='yellow', tags='disco')
        desenhar_torre(self.torre_a, self.posicoes[0])
        desenhar_torre(self.torre_b, self.posicoes[1])
        desenhar_torre(self.torre_c, self.posicoes[2])

    def mover_disco(self, origem, destino):
        if origem and (not destino or origem[-1] < destino[-1]):
            disco = origem.pop()
            destino.append(disco)
            self.movimentos += 1
            self.lbl_movimentos.config(text=f'Movimentos: {self.movimentos}')
            self.mostrar_discos()
            self.verificar()
        else:
            messagebox.showwarning('Aviso!', 'Movimento inválido!')

    def verificar(self):
        if len(self.torre_c) == self.discos:
            messagebox.showinfo('Parabéns!', f'Você venceu em {self.movimentos} movimentos.')

    def selecionar_torre(self, torre):
        if self.selecionada is None:
            self.selecionada = torre
        else:
            if self.selecionada != torre:
                origem = getattr(self, f'torre_{self.selecionada.lower()}')
                destino = getattr(self, f'torre_{torre.lower()}')
                self.mover_disco(origem, destino)
            self.selecionada = None

janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
