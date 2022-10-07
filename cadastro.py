import tkinter as tk
from tkinter import ttk
import datetime as dt

janela = tk.Tk()

#Titulo da Janela

janela.title('Ferramenta de cadastro de materiais')

label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(row=1, column=0)

janela.mainloop()
