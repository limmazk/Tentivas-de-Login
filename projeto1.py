import tkinter as tk
from tkinter import messagebox

falhas_de_login = 0
historico_login = []


def verificar_login():
    global falhas_de_login
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == "admin" and senha == "euadmin":
        historico_login.append(f"Login bem-sucedido: {usuario}")
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        abrir_painel_admin()
    else:
        falhas_de_login += 1
        historico_login.append(f"Falha de login: {usuario}")
        messagebox.showinfo("Erro", "Usuário ou senha incorretos")

def abrir_painel_admin():
    nova_janela = tk.Toplevel()
    nova_janela.title("Painel do Admin")

    rotulo_falhas = tk.Label(nova_janela, text=f"Total de falhas de login: {falhas_de_login}")
    rotulo_falhas.pack(pady=10)

    rotulo_historico = tk.Label(nova_janela, text="Históricos de Logins:")
    rotulo_historico.pack(pady=5)

    text_area = tk.Text(nova_janela, wrap=tk.WORD, width=60, height=10)
    for log in historico_login:
        text_area.insert(tk.END, log + "\n")
    text_area.pack()


janela = tk.Tk()
janela.title("Login de Usuário")

janela.geometry("400x200")

rotulo_usuario = tk.Label(janela, text="Usuário:")
rotulo_usuario.pack(pady=5)
entrada_usuario = tk.Entry(janela, width=40)
entrada_usuario.pack(pady=5)

rotulo_senha = tk.Label(janela, text="Senha:")
rotulo_senha.pack(pady=5)
entrada_senha = tk.Entry(janela, show="*",  width=40)
entrada_senha.pack(pady=5)

botao_login = tk.Button(janela, text="Login", command=verificar_login)
botao_login.pack(pady=20)

janela.mainloop()