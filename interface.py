from tkinter import *
from domain import *
from ip_enumeration import *

domain_result_file_name = 'relatorio_final.txt'
ips_result_file_name = 'relatorio_final_ips.txt'

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Consultar dominio")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.dominioLabel = Label(self.segundoContainer,text="Dominio", font=self.fontePadrao)
        self.dominioLabel.pack(side=LEFT)

        self.dominio = Entry(self.segundoContainer)
        self.dominio["width"] = 30
        self.dominio["font"] = self.fontePadrao
        self.dominio.bind( "<Return>")
        self.dominio.pack(side=LEFT)

        self.consultar = Button(self.terceiroContainer)
        self.consultar["text"] = "Consultar"
        self.consultar["font"] = ("Calibri", "8")
        self.consultar["width"] = 12
        self.consultar.bind("<Return>") 
        self.consultar["command"] = self.verificaDominio
        self.consultar.pack()

        self.mensagem = Label(self.terceiroContainer,text="", font=self.fontePadrao)
        self.mensagem.pack()

    def verificaDominio(self):
        inputDominio = self.dominio.get()
        exec_tools(inputDominio, domain_result_file_name)
        enumerate_ips(domain_result_file_name, ips_result_file_name)

    def carregando(self, event):
        self.mensagem["text"] = "Carregando..."

        
root = Tk()
Application(root)
root.mainloop()


