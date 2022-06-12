from tkinter import *
import cores as cor

root = Tk()

class Botoes:
    def __init__(self,master,Texto):
        self.botao = Button(master)
        self.botao.configure(
            text=Texto,
            bg=cor.cinza_escuro,
            fg=cor.branco,
            relief=FLAT,
        )

class App:
    def __init__(self):
        self.root = root
        self.Tela()
        self.Frames_Tela()
        self.criar_Botoes()
        self.root.mainloop()

    def Tela(self):
        self.root.title("Aprendendo Classes")
        self.root.configure(background=cor.azul_escuro_pastel)
        self.root.geometry('700x500')
        self.root.resizable(True,True)
        self.root.maxsize(width='900', height='700')
        self.root.minsize(width='500', height='400')

    def Frames_Tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.configure(
            bd = 4,
            bg = cor.cinza_azulado_claro,
            highlightbackground= cor.marrom_claro,
            highlightthickness=3,
        )
        self.frame_1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.46)
        
        self.frame_2 = Frame(self.root)
        self.frame_2.configure(
            bd = 4,
            bg = cor.cinza_azulado_claro,
            highlightbackground= cor.marrom_claro,
            highlightthickness=3,
        )
        self.frame_2.place(relx=0.02,rely=0.5,relwidth=0.96,relheight=0.46)

    def criar_Botoes(self):
        self.bt_Limpar = Botoes(self.root,'Limpar')
        self.bt_Limpar.botao.place(relx=0.2,rely=0.1, relwidth=0.1, relheight=0.05)
        self.bt_Buscar = Botoes(self.root,'Buscar')
        self.bt_Buscar.botao.place(relx=0.31,rely=0.1, relwidth=0.1, relheight=0.05)
        self.bt_Novo = Botoes(self.root,'Novo')
        self.bt_Novo.botao.place(relx=0.6,rely=0.1, relwidth=0.1, relheight=0.05)
        self.bt_Alterar = Botoes(self.root,'Alterar')
        self.bt_Alterar.botao.place(relx=0.71,rely=0.1, relwidth=0.1, relheight=0.05)
        self.bt_Apagar = Botoes(self.root,'Apagar')
        self.bt_Apagar.botao.place(relx=0.82,rely=0.1, relwidth=0.1, relheight=0.05)
App()