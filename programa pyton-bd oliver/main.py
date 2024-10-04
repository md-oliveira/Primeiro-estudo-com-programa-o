import sqlite3
import locale
from tkinter import*
from tkinter import ttk, messagebox 
import tkinter as tk
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
entrada_nome = None
quantidade_entrada = None
entrada_preco = None
tabela = None
informacoes_usuarios = None
informacoes = None
final_botao = None
entry_nome = None
entry_senha = None



def abrir_janela_cadastro():
                
                cadastro = Tk()
                cadastro.geometry("2000x2000")
                cadastro.title("Cadastro")
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

                cadastro_botao = Button(cadastro, text="Começar", fg="black")
                cadastro_botao.pack(pady=50)

                cadastro.mainloop()


    ###############################################################################
def salvar_cadastro(nome, senha):
    
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            nome TEXT,
            senha TEXT
        )
    ''')

    cursor.execute('INSERT INTO usuarios (nome, senha) VALUES (?, ?)',
                   (nome, senha))

    conn.commit()
    conn.close()
def abrir_janela_logon():
            global entry_nome, entry_senha
            cadastro = Tk()
            cadastro.geometry("2000x2000")
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

            cadastro_botao = Button(cadastro, text="Começar", fg="black", command=abrir_janela_principal)
            cadastro_botao.pack(pady=50)

            cadastro.mainloop()
        
        

    ##############################################################################
def salvar_e_abrir_principal():
    global entry_nome, entry_senha
    nome = entry_nome.get()
    senha = entry_senha.get()
    salvar_cadastro(nome, senha)
    carregar_dados_tabela(tabela)
def carregar_dados_tabela(tabela):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    # Selecionando apenas o campo 'nome' da tabela 'usuarios'
    cursor.execute('SELECT nome FROM usuarios')
    nomes = cursor.fetchall()

    # Limpando a tabela antes de carregar novos dados
    for item in tabela.get_children():
        tabela.delete(item)

    # Inserindo os nomes na tabela
    for nome in nomes:
        tabela.insert("", "end", values=(nome[0],))  # Usamos nome[0] para pegar o primeiro elemento da tupla

    conn.close()
def abrir_janela_principal ():
        
    #interface principal
    global entry_nome, entry_senha
    janela = Tk()
    janela.geometry("2000x2000")
    janela.title("Início")

    texto1 = Label(janela, text="O que deseja fazer hoje?",justify='center',bg="#474747", fg="white", bd=0, relief='flat')
    texto1.pack( padx=(20,0), pady=20)

    botao1 = Button(janela, text= "Cadastrar produtos",width=15, command=planilha)
    botao1.pack(padx=(20,0),ipadx=10, side="top",pady=(150, 20),)

    botao2 = Button(janela, text="Gasto mensal",width=15)
    botao2.pack(padx=(20,0), pady=20,ipadx=10,  side="top")

    botao3 = Button(janela, text="Gasto anual",width=15)
    botao3.pack(padx=(20,0), pady=20,ipadx=10, side="top")

    botao4 = Button(janela, text = "Usuários",width=15, command=usuarios) 
    botao4.pack(padx=(20,0), pady=20,ipadx=10,  side="top")

    # mudando background
    janela.configure(bg="#474747")

    # Criando uma cor personalizada (RGB)
    cor_personalizada = "#474747"
    janela.mainloop()
            
    
    #####################################################################################################################################
def mensagem_De_Cadastro():
    global entry_nome, entry_senha
    mensagem = Tk()
    mensagem.geometry("2000x2000")
    mensagem.title("Boas vindas")

    mensagem_cadastro = Label(mensagem, text="Cadastro realizado !" , bg="#474747", fg="white", bd=0, relief='flat')
    mensagem_cadastro.pack()

    botao = Button(mensagem, text="Continuar", command=abrir_janela_principal) 
    botao.pack(pady=50)
    
    mensagem.configure(bg ="#474747")
    mensagem.mainloop()
def escolha_mes():   
 
    selecao_mes = Tk()
    selecao_mes.geometry("300x300")
    selecao_mes.title("Escolha o mês da compra")  


    rotulo_mes = Label(selecao_mes, text="Selecione o mês da compra", fg="white", bg="#474747")
    rotulo_mes.pack(side="top")

    selecao_mes.configure(bg="#474747")

    
    # Criar uma combobox para selecionar o mês
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    mes_selecionado = StringVar()
    mes_combobox = ttk.Combobox(selecao_mes, textvariable=mes_selecionado, values=meses, state='readonly')
    mes_combobox.set('Selecione o Mês')
    mes_combobox.pack(pady= 5, anchor='w', padx=60)
    
    botao_mes = Button(selecao_mes, text="Confirmar")
    botao_mes.pack(pady=15, padx=60)
    selecao_mes.mainloop()
def cadastrar_produto():
    global entrada_nome, quantidade_entrada, entrada_preco, tabela, final_botao

    # Obter dados inseridos nas entradas
    nome_produto = entrada_nome.get()
    quantidade = quantidade_entrada.get()
    preco_str = entrada_preco.get()

    # Verificar se todos os campos estão preenchidos
    if nome_produto and quantidade and preco_str:
        # Verificar se a quantidade é um número inteiro
        if not quantidade.isdigit():
            # Mostrar aviso se a quantidade não for um número inteiro
            messagebox.showwarning("Formato Inválido", "O campo de 'Quantidade' deve ser preenchido com números inteiros.")
            return  # Parar a execução se a quantidade não for válida

        # Substituir vírgulas por pontos no campo de preço
        preco_str = preco_str.replace(',', '.')

        try:
            # Tentar converter o preço para um número de ponto flutuante
            preco = float(preco_str)
        except ValueError:
            # Mostrar aviso se o preço não puder ser convertido para um número
            messagebox.showwarning("Formato Inválido", "O campo de 'Preço' deve ser preenchido com um número válido.")
            return  # Parar a execução se o preço não for válido

        # Inserir dados na tabela com formatação correta
        tabela.insert('', 'end', values=(nome_produto, quantidade, f'R${preco:,.2f}'))

        # Limpar as entradas após o cadastro
        entrada_nome.delete(0, 'end')
        quantidade_entrada.delete(0, 'end')
        entrada_preco.delete(0, 'end')

        # Atualizar o estado do botão após inserir um novo item
        habilitar_botao()
    else:
        # Mostrar aviso caso algum campo esteja vazio
        messagebox.showwarning("Campos Vazios", "Todos os campos devem ser preenchidos.")
def finalizar_cadastro():
    if len(tabela.get_children()) > 0:
        messagebox.showinfo("Cadastro Finalizado", "O cadastro foi finalizado com sucesso!")
        informacoes.destroy()
    else:
        messagebox.showwarning("Nenhum Item", "Você precisa cadastrar pelo menos um item antes de finalizar o cadastro.")
def habilitar_botao():
    if len(tabela.get_children()) > 0:
        final_botao['state'] = NORMAL
    else:
        final_botao['state'] = DISABLED
def planilha():
    global entrada_nome, quantidade_entrada, entrada_preco, tabela, final_botao

    informacoes = Tk()
    informacoes.geometry("2000x2000")
    informacoes.title("Cadastro de produtos")

    informacoes_nome = Label(informacoes, text="Nome do produto:", bg="#474747", fg="white")
    informacoes_nome.pack(pady=10, anchor='w')  
    entrada_nome = Entry(informacoes)
    entrada_nome.pack(pady=10, anchor="w")

    quantidade_label = Label(informacoes, text="Quantidade", bg="#474747", fg="white")
    quantidade_label.pack(pady=10, anchor='w')
    quantidade_entrada = Entry(informacoes)
    quantidade_entrada.pack(pady=10, anchor='w')

    informacoes_preco = Label(informacoes, text="Preço unitário:", bg="#474747", fg="white")
    informacoes_preco.pack(pady=10, anchor='w')
    entrada_preco = Entry(informacoes)
    entrada_preco.pack(pady=10, anchor="w")

    planilha_botao = Button(informacoes, text="Cadastrar Produto", command=cadastrar_produto)
    planilha_botao.pack(pady=20, anchor='w')

    prox_botao = Button(informacoes, text="Escolha de mês", command=escolha_mes)
    prox_botao.pack(pady=20, anchor='w')

    #criando tabela
    tabela = ttk.Treeview(informacoes, columns=('Nome', 'Quantidade', 'Preço'), show='headings')
    tabela.heading('Nome', text='Nome')
    tabela.heading('Quantidade', text='Quantidade')
    tabela.heading('Preço', text='Preço')
    tabela.place(relx=0.5, rely=0.15, anchor='n') 

    # Botão para finalizar cadastro
    final_botao = Button(informacoes, text="Finalizar cadastro", state=DISABLED, command=finalizar_cadastro)
    final_botao.place(relx=0.98, rely=0.15, anchor='ne')
    
    # Inicializar o estado do botão
    habilitar_botao()
   
   
   
   
   
   
   
    informacoes.configure (bg="#474747")
def usuarios():
    informacoes_usuarios = Tk()
    informacoes_usuarios.geometry("2000x2000")
    informacoes_usuarios.title("Usuários")

    # Criando tabela
    tabela = ttk.Treeview(informacoes_usuarios, columns=('Nome'), show='headings')

    # Configurando o título da coluna
    tabela.heading('Nome', text='Usuários')

    tabela.place(relx=0.5, rely=0.15, anchor='n', relheight=0.5, relwidth=0.4) 

    # Carregando dados na tabela
    carregar_dados_tabela(tabela)

    informacoes_usuarios.mainloop()



abrir_janela_principal ()



  







































































#################################################################################################################################################
#logon

# Criando a parte de logon
                
janela1 = Tk()

# Tamanho da janela
janela1.geometry("2000x2000")

# Mudando o título
janela1.title("LOGIN")

 # mudando background
janela1.configure(bg="#474747")

 # Criando uma cor personalizada (RGB)
cor_personalizada = "#474747"

# Inserindo texto na janela
boas_vindas1 = Label(janela1, text="Seja bem vindo ao seu contabilizador de gastos",bg="#474747", fg="white", bd=0, relief='flat')
boas_vindas1.pack(padx=(20, 0), pady=(20, 55))
boas_vindas1.pack(padx=(20, 0), pady=(20, 55)) 
boas_vindas2 = Label(janela1, text="Escolha uma opção",bg="#474747", fg="white", bd=0, relief='flat')
boas_vindas2.pack(padx=(20, 0), pady=20)


botao1 = Button(janela1, text= "Cadastrar",width=15,command=abrir_janela_cadastro)
botao1.pack(padx=(20,0),ipadx=10, side="top",pady=(15, 20),)

botao2 = Button(janela1, text="Entrar ",width=15,command=abrir_janela_logon)
botao2.pack(padx=(20,0), pady=20,ipadx=10,  side="top", )

# Iniciando o loop principal do tkinter
janela1.mainloop()



##############################################################################
