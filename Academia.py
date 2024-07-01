import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AcademiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("      ACADEMIA      ")
        self.root.geometry("500x400")
        self.root.configure(bg="#778da9")  # Set background color

        self.cpf = 0
        self.usuarios = {}  # Dicionário para armazenar usuários cadastrados
        self.treinos = {} 

        self.nome = "João da Silva"
        self.email = "joao.silva@example.com"
        self.status_pagamento = "Pago"
        self.data_pagamento = "01/07/2024"

        treino_padrao(self)

        self.frame_login = tk.Frame(self.root, bg="#778da9")
        self.frame_registro = tk.Frame(self.root, bg="#778da9")
        self.frame_treino = tk.Frame(self.root, bg="#778da9")
        self.frame_criartreino = tk.Frame(self.root, bg="#778da9")
        self.frame_usuario = tk.Frame(self.root, bg="#778da9")
        self.frame_pagamento = tk.Frame(self.root, bg="#778da9")


        self.frame_login.pack(expand=True, fill='both', padx=20, pady=20)
        self.frame_registro.pack(expand=True, fill='both', padx=20, pady=20)
        self.frame_treino.pack(expand=True, fill='both', padx=20, pady=20)
        self.frame_criartreino.pack(expand=True, fill='both', padx=20, pady=20)
        self.frame_usuario.pack(expand=True, fill='both', padx=20, pady=20)
        self.frame_pagamento.pack(expand=True, fill='both', padx=20, pady=20)

        self.show_frame("login")

    def show_frame(self, frame):
        self.frame_login.pack_forget()
        self.frame_registro.pack_forget()
        self.frame_usuario.pack_forget()
        self.frame_pagamento.pack_forget()
        self.frame_treino.pack_forget()
        self.frame_criartreino.pack_forget()


 
        if frame == "login":
            self.frame_login.pack(expand=True, fill='both', padx=20, pady=20)
            self.criar_tela_login()
        elif frame == "registro":
            self.frame_registro.pack(expand=True, fill='both', padx=20, pady=20)
            self.criar_tela_registro()
        elif frame == "treino":
            self.frame_treino.pack(expand=True, fill='both', padx=20, pady=20)
            self.criar_tela_treino()
        elif frame == "criartreino":
            self.frame_criartreino.pack(expand=True, fill='both', padx=20, pady=20)
            self.criartreino()

        elif frame == "pagamento":
            self.frame_pagamento.pack(expand=True, fill='both', padx=50, pady=50)
            self.criar_tela_pagamento()

    def fazer_login(self):
        cpf = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if cpf in self.usuarios:
            if self.usuarios[cpf] == senha:
                messagebox.showinfo("Login", "USUÁRIO AUTENTICADO COM SUCESSO!")
                self.show_frame("treino")
            else:
                messagebox.showerror("Erro", "CPF OU SENHA INCORRETOS.")
        else:
            messagebox.showerror("Erro", "CPF NÃO CADASTRADO.")

    def fazer_registro(self):
        cpf = self.entry_cpf.get()
        senha = self.entry_senha_registro.get()

        if cpf in self.usuarios:
            messagebox.showerror("Erro", "CPF JÁ CADASTRADO!")
        else:
            self.usuarios[cpf] = senha
            messagebox.showinfo("Registro", "USUÁRIO REGISTRADO COM SUCESSO!")
            self.show_frame("login")

    def criar_tela_login(self):
        # Limpar a tela antes de criar os widgets
        for widget in self.frame_login.winfo_children():
            widget.destroy()

        #Cabeçalho
        label_login = tk.Label(self.frame_login, text="LOGIN", fg="#000000", bg="#778da9", font=("Segoe UI", 20))
        label_login.pack(pady=2) 


        # Criar os widgets
        
        label_usuario = tk.Label(self.frame_login, text="CPF:", fg="#000000", bg="#778da9")
        label_senha = tk.Label(self.frame_login, text="SENHA:", fg="#000000", bg="#778da9")
        self.entry_usuario = tk.Entry(self.frame_login, width=25)
        self.entry_senha = tk.Entry(self.frame_login, show="*", width=25)
        btn_login = tk.Button(self.frame_login, text="LOGIN", command=self.fazer_login, bg="#90e0ef", fg="#000000", padx=0, pady=0, width=1, height=2)
        btn_ir_para_registro = tk.Button(self.frame_login, text="REGISTRAR", command=lambda: self.show_frame("registro"), bg="#90e0ef", fg="#000000", padx=0, width=1, height=2)

        label_login.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
        label_usuario.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        label_senha.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_senha.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        btn_login.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        btn_ir_para_registro.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        # Centralizar os widgets
        self.frame_login.grid_rowconfigure(0, weight=1)
        self.frame_login.grid_rowconfigure(1, weight=1)
        self.frame_login.grid_rowconfigure(2, weight=1)
        self.frame_login.grid_rowconfigure(3, weight=1)
        self.frame_login.grid_columnconfigure(0, weight=1)
        self.frame_login.grid_columnconfigure(1, weight=1)

    def criar_tela_registro(self):
        # Limpar a tela antes de criar os widgets
        for widget in self.frame_registro.winfo_children():
            widget.destroy()

        label_registro = tk.Label(self.frame_registro, text="REGISTRO", fg="#000000", bg="#778da9", font=("Segoe UI", 24))
        label_cpf = tk.Label(self.frame_registro, text="CPF:", fg="#000000", bg="#778da9")
        self.entry_cpf = tk.Entry(self.frame_registro, width=25)
        label_senha_registro = tk.Label(self.frame_registro, text="SENHA:", fg="#000000", bg="#778da9")
        self.entry_senha_registro = tk.Entry(self.frame_registro, show="*", width=25)
        btn_registro = tk.Button(self.frame_registro, text="REGISTRO", command=self.fazer_registro, bg="#90e0ef", fg="#000000", width=20)
        btn_voltar_login = tk.Button(self.frame_registro, text="VOLTAR PARA O LOGIN", command=lambda: self.show_frame("login"), bg="#90e0ef", fg="#000000", width=20)

        label_registro.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        label_cpf.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_cpf.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        label_senha_registro.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_senha_registro.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        btn_registro.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        btn_voltar_login.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        # Centralizar os widgets
        self.frame_registro.grid_rowconfigure(0, weight=1)
        self.frame_registro.grid_rowconfigure(1, weight=1)
        self.frame_registro.grid_rowconfigure(2, weight=1)
        self.frame_registro.grid_rowconfigure(3, weight=1)
        self.frame_registro.grid_rowconfigure(4, weight=1)
        self.frame_registro.grid_columnconfigure(0, weight=1)
        self.frame_registro.grid_columnconfigure(1, weight=1)
 

    def criar_tela_pagamento(self):
        for widget in self.frame_pagamento.winfo_children():
            widget.destroy()

        label_pagamento = tk.Label(self.frame_pagamento, text="Informações de Pagamento", fg="#FFD700", bg="#000000", font=("Helvetica", 16))
        label_status_pagamento = tk.Label(self.frame_pagamento, text=f"Status do Pagamento: {self.status_pagamento}", fg="#FFD700", bg="#000000", font=("Helvetica", 14))
        label_data_pagamento = tk.Label(self.frame_pagamento, text=f"Data do Pagamento: {self.data_pagamento}", fg="#FFD700", bg="#000000", font=("Helvetica", 14))
        btn_voltar = tk.Button(self.frame_pagamento, text="Voltar", command=lambda: self.show_frame("treino"), bg="#FFD700", fg="#000000")

        label_pagamento.grid(row=0, column=0, columnspan=2, pady=10)
        label_status_pagamento.grid(row=1, column=0, columnspan=2, pady=5)
        label_data_pagamento.grid(row=2, column=0, columnspan=2, pady=5)
        btn_voltar.grid(row=3, column=0, columnspan=2, pady=10)

        # Centralizar widgets na tela
        self.frame_pagamento.grid_rowconfigure(0, weight=1)
        self.frame_pagamento.grid_rowconfigure(1, weight=1)
        self.frame_pagamento.grid_rowconfigure(2, weight=1)
        self.frame_pagamento.grid_rowconfigure(3, weight=1)
        self.frame_pagamento.grid_columnconfigure(0, weight=1)
            

    def criar_tela_treino(self):
        # Limpar a tela antes de criar os widgets
        for widget in self.frame_treino.winfo_children():
            widget.destroy()

        label_treino = tk.Label(self.frame_treino, text="ESCOLHA O DIA DA SEMANA:", fg="#000000", bg="#778da9", font=("Segoe UI", 16))
        btn_segunda = tk.Button(self.frame_treino, text="SEGUNDA-FEIRA", command=lambda: self.mostrar_treino("Segunda"), bg="#90e0ef", fg="#000000", width=20)
        btn_terca = tk.Button(self.frame_treino, text="TERÇA-FEIRA", command=lambda: self.mostrar_treino("Terça"), bg="#90e0ef", fg="#000000", width=20)
        btn_quarta = tk.Button(self.frame_treino, text="QUARTA-FEIRA", command=lambda: self.mostrar_treino("Quarta"), bg="#90e0ef", fg="#000000", width=20)
        btn_quinta = tk.Button(self.frame_treino, text="QUINTA-FEIRA", command=lambda: self.mostrar_treino("Quinta"), bg="#90e0ef", fg="#000000", width=20)
        btn_sexta = tk.Button(self.frame_treino, text="SEXTA-FEIRA", command=lambda: self.mostrar_treino("Sexta"), bg="#90e0ef", fg="#000000", width=20)
        btn_voltar = tk.Button(self.frame_treino, text="VOLTAR", command=lambda: self.show_frame("login"), bg="#90e0ef", fg="#000000", width=20)
        btn_criartreino = tk.Button(self.frame_treino, text="CRIAR TRIENO", command=lambda: self.show_frame("criartreino"), bg="#90e0ef", fg="#000000", width=20)

        label_treino.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        btn_segunda.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        btn_terca.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        btn_quarta.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        btn_quinta.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        btn_sexta.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        btn_criartreino.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        btn_voltar.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        # Centralizar os widgets
        self.frame_treino.grid_rowconfigure(0, weight=1)
        self.frame_treino.grid_rowconfigure(1, weight=1)
        self.frame_treino.grid_rowconfigure(2, weight=1)
        self.frame_treino.grid_rowconfigure(3, weight=1)
        self.frame_treino.grid_rowconfigure(4, weight=1)
        self.frame_treino.grid_rowconfigure(5, weight=1)
        self.frame_treino.grid_rowconfigure(6, weight=1)
        self.frame_treino.grid_rowconfigure(7, weight=1)
        self.frame_treino.grid_columnconfigure(0, weight=1)
        self.frame_treino.grid_columnconfigure(1, weight=1)

    def criartreino(self):

        for widget in self.frame_criartreino.winfo_children():
            widget.destroy()

        lbl_titulo = tk.Label(self.frame_criartreino, text="Título:", fg="#000000", bg="#778da9")
        lbl_titulo.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_titulo = tk.Entry(self.frame_criartreino, width=50)
        self.entry_titulo.grid(row=0, column=1, padx=10, pady=5)

        # Descrição
        lbl_descricao = tk.Label(self.frame_criartreino, text="Descrição:", fg="#000000", bg="#778da9")
        lbl_descricao.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.text_descricao = tk.Text(self.frame_criartreino, width=50, height=5)
        self.text_descricao.grid(row=1, column=1, padx=10, pady=5)

        # Combobox
        self.opcoes = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        self.opcao_selecionada = tk.StringVar()
        self.combobox = ttk.Combobox(self.frame_criartreino, textvariable=self.opcao_selecionada, width=25)
        self.combobox['values'] = self.opcoes
        self.combobox['state'] = 'readonly' 
        self.combobox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Botões
        btn_salvar = tk.Button(self.frame_criartreino, text="SALVAR", command=self.salvar, bg="#90e0ef", fg="#000000", width=10)
        btn_voltar = tk.Button(self.frame_criartreino, text="VOLTAR", command=lambda: self.show_frame("treino"), bg="#90e0ef", fg="#000000", width=10)
        btn_pagamento = tk.Button(self.frame_criartreino, text="STATUS", command=lambda: self.show_frame("pagamento"), bg="#90e0ef", fg="#000000", width=10)

        btn_salvar.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        btn_voltar.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        btn_pagamento.grid(row=5, column=1, padx=10, pady=10, sticky="w")


    def salvar(self):
        titulo = self.entry_titulo.get()
        descricao = self.text_descricao.get("1.0", tk.END)
        texto = titulo + "\n\n" + descricao

        self.treinos[self.opcao_selecionada.get()] = texto
        messagebox.showinfo("Salvo", "O treino foi salvo")


    def mostrar_treino(self, dia):

        messagebox.showinfo(dia, self.treinos[dia])

    def tela_treino(self):
        nome = self.nome_entry.get()
        descricao = self.descricao_text.get("1.0", "end-1c")

        treino = f"""Treino: {nome}Descrição: 
        {descricao}"""
        messagebox.showinfo("Novo Treino", treino)

def criar_treino():
    root = tk.Tk()
    app = criar_treino(root)
    root.mainloop()

def treino_padrao(self):
    self.treinos["Segunda"] = """
            TREINO DE QUADRÍCEPS

            AQUECIMENTO:
             - 5-10 minutos de cardio leve.

            - AGACHAMENTO LIVRE:
             - 4 séries de 8-10 repetições.
             - Descanse 90 segundos entre as séries.

            - LEG PRESS:
             - 4 séries de 10-12 repetições.
             - Descanse 90 segundos entre as séries.

            - CADEIRA EXTENSORA:
             - 3 séries de 12-15 repetições.
             - Descanse 60 segundos entre as séries.

            - AFUNDO COM HALTERES:
             - 3 séries de 10-12 repetições.
             - Descanse 60 segundos entre as séries.

            - PANTURRILHA SENTADA:
             - 4 séries de 12-15 repetições.
             - Descanse 60 segundos entre as séries.
            """
    self.treinos["Terça"] = """
            TREINO DE BÍCEPS, OMBROS E ABDÔMEN

            AQUECIMENTO:
             - 5-10 minutos de cardio leve.

            - ROSCA DIRETA COM BARRA:
             - 4 séries de 8-10 repetições.
             - Descanse 90 segundos entre as séries.

            - ROSCA MARTELO COM HALTERES:
             - 4 séries de 10-12 repetições (cada braço).
             - Descanse 90 segundos entre as séries.

            - DESENVOLVIMENTO COM HALTERES:
             - 4 séries de 8-10 repetições.
             - Descanse 90 segundos entre as séries.

            - ELEVAÇÃO LATERAL COM HALTERES:
             - 3 séries de 10-12 repetições.
             - Descanse 60 segundos entre as séries.

            - ELEVAÇÃO FRONTAL COM HALTERES:
             - 3 séries de 10-12 repetições.
             - Descanse 60 segundos entre as séries.
            """
    self.treinos["Quarta"] = """
            TREINO DE POSTERIOR DE COXA (Isquiotibiais)

            AQUECIMENTO:
             - 5-10 minutos de cardio leve.

            - MESA FLEXORA (posterior deitada):
             - 4 séries de 10-12 repetições.
             - Descanse 90 segundos entre as séries.

            - PASSADA:
             - 3 séries de ida e volta.
             - Descanse 120 segundos entre as séries.

            - CADEIRA FLEXORA:
             - 3 séries de 12-15 repetições.
             - Descanse 60 segundos entre as séries.

            - CADEIRA ABDUTORA:
             - 4 séries de 12-15 repetições.
             - Descanse 60 segundos entre as séries.

            - PANTURRILHA EM PÉ:
             - 3 séries de 12-15 repetições.
             - Descanse 60 segundos entre as séries.
            """
    self.treinos["Quinta"] = """
            TREINO DE COSTAS, TRÍCEPS E PEITO

            AQUECIMENTO:
             - 5-10 minutos de cardio leve.

            - BARRA FIXA OU PUXADA ALTA (com máquina ou barra fixa):
             - 4 séries de 8-10 repetições.
             - Descanse 90 segundos entre as séries.

            - REMADA BAIXA:
             - 4 séries de 8-10 repetições.
             - Descanse 90 segundos entre as séries.

            - SUPINO RETO COM BARRA OU HALTERES:
             - 4 séries de 8-10 repetições.
             - Descanse 90 segundos entre as séries.

            - PECK DECK:
             - 3 séries de 10-12 repetições.
             - Descanso de 60 segundos entre as séries.

            - TRÍCEPS PULLEY CORDA:
             - 3 séries de 10-12 repetições.
             - Descanse 60 segundos entre as séries.

            - TRÍCEPS TESTA:
             - 3 séries de 10-12 repetições.
             - Descanse 60 segundos entre as séries.
            """
    self.treinos["Sexta"] = """
            TREINO DE GLÚTEOS

            AQUECIMENTO:
             - 5-10 minutos de cardio leve.

            - AGACHAMENTO SUMÔ:
             - 4 séries de 8-10 repetições.
             - Descanse 90 segundos entre as séries.

            - ELEVAÇÃO PÉLVICA (Glúteo Bridge):
             - 4 séries de 10-12 repetições.
             - Descanse 90 segundos entre as séries.

            - CADEIRA ABDUTORA:
             - 3 séries de 12-15 repetições.
             - Descanse 60 segundos entre as séries.

            - AGACHAMENTO HACK:
             - 4 séries de 10-12 repetições.
             - Descanse 60 segundos entre as séries.

            - PANTURRILHA EM PÉ:
             - 3 séries de 12-15 repetições.
             - Descanse 60 segundos entre as séries.
            """
def main():
    root = tk.Tk()
    academia_app = AcademiaApp(root)
    root.mainloop()



if __name__ == "__main__":
    main()