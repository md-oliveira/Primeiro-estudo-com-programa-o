from tkinter import *
import sqlite3

def criar_tabela():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nome TEXT, senha TEXT)")
    conn.commit()
    conn.close()

def salvar_informacoes():
    nome = entry_nome.get()
    senha = entry_senha.get()

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
    conn.commit()
    conn.close()

    # Após salvar as informações, exibir a mensagem de cadastro
    mensagem_De_Cadastro()

def abrir_janela_logon():
    global entry_nome, entry_senha
    criar_tabela()

    cadastro = Tk()
    cadastro.geometry("400x200")
    cadastro.title("Logon")
    cadastro.configure(bg="#474747")

    texto_cadastro = Label(cadastro, text="Insira suas informações", bg="#474747", fg="white")
    texto_cadastro.pack(pady=20)

    label_nome = Label(cadastro, text="Nome:", bg="#474747", fg="white")
    label_nome.pack()
    entry_nome = Entry(cadastro)
    entry_nome.pack(pady=10)

    label_senha = Label(cadastro, text="Senha:", bg="#474747", fg="white")
    label_senha.pack()
    entry_senha = Entry(cadastro, show="*")
    entry_senha.pack(pady=10)

    cadastro_botao_voltar = Button(cadastro, text="Voltar", fg="black", command=cadastro.destroy)
    cadastro_botao_voltar.pack(side=LEFT, anchor=NW, padx=10, pady=10)

    cadastro_botao = Button(cadastro, text="Começar", fg="black", command=salvar_informacoes)
    cadastro_botao.pack(side=TOP, anchor=CENTER, pady=50)

    cadastro.mainloop()

def abrir_janela_principal():
    print("Abrir janela principal")

def mensagem_De_Cadastro():
    mensagem = Tk()
    mensagem.geometry("400x200")
    mensagem.title("Boas vindas")
    mensagem.configure(bg="#474747")

    mensagem_cadastro = Label(mensagem, text="Cadastro realizado!", bg="#474747", fg="white")
    mensagem_cadastro.pack(pady=20)

    botao = Button(mensagem, text="Continuar", command=mensagem.destroy)
    botao.pack(pady=20)

    mensagem.mainloop()

janela1 = Tk()
janela1.geometry("400x400")
janela1.title("LOGIN")
janela1.configure(bg="#474747")

boas_vindas1 = Label(janela1, text="Seja bem vindo ao seu contabilizador de gastos", bg="#474747", fg="white", bd=0, relief='flat')
boas_vindas1.pack(padx=(20, 0), pady=(20, 55))
boas_vindas2 = Label(janela1, text="Escolha uma opção", bg="#474747", fg="white", bd=0, relief='flat')
boas_vindas2.pack(padx=(20, 0), pady=20)

botao1 = Button(janela1, text="Cadastrar", width=15, command=abrir_janela_logon)
botao1.pack(padx=(20,0), ipadx=10, side="top", pady=(15, 20))

botao2 = Button(janela1, text="Entrar", width=15)
botao2.pack(padx=(20,0), pady=20, ipadx=10,  side="top")

janela1.mainloop()
