import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Configurações da base de dados
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',  # Substitua pelo seu utilizador do MySQL
    'password': 'sua_palavra_passe',  # Substitua pela sua palavra-passe
    'database': 'lista_convidados'
}

# Função para criar a tabela no MySQL
def criar_tabela():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS convidados (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                email VARCHAR(255),
                palavra_passe VARCHAR(255)
            )
        """)
        conn.commit()
        conn.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Erro na Base de Dados", f"Erro: {e}")

# Função para adicionar um convidado
def adicionar_convidado():
    nome = nome_entry.get()
    email = email_entry.get()
    palavra_passe = palavra_passe_entry.get()

    if not nome or not email or not palavra_passe:
        messagebox.showwarning("Campos Vazios", "Todos os campos são obrigatórios.")
        return

    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO convidados (nome, email, palavra_passe) VALUES (%s, %s, %s)", 
                       (nome, email, palavra_passe))
        conn.commit()
        conn.close()
        listar_convidados()
        limpar_campos()
    except mysql.connector.Error as e:
        messagebox.showerror("Erro na Base de Dados", f"Erro: {e}")

# Função para remover um convidado
def remover_convidado():
    try:
        selecionado = lista_convidados.curselection()
        if not selecionado:
            messagebox.showwarning("Seleção Inválida", "Selecione um convidado para remover.")
            return

        convidado = lista_convidados.get(selecionado)
        convidado_id = convidado.split(":")[0]  # ID do convidado

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM convidados WHERE id = %s", (convidado_id,))
        conn.commit()
        conn.close()
        listar_convidados()
    except mysql.connector.Error as e:
        messagebox.showerror("Erro na Base de Dados", f"Erro: {e}")

# Função para listar convidados
def listar_convidados():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM convidados")
        convidados = cursor.fetchall()
        conn.close()

        lista_convidados.delete(0, tk.END)
        for convidado in convidados:
            lista_convidados.insert(tk.END, f"{convidado[0]}: {convidado[1]} ({convidado[2]})")
    except mysql.connector.Error as e:
        messagebox.showerror("Erro na Base de Dados", f"Erro: {e}")

# Função para limpar campos
def limpar_campos():
    nome_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    palavra_passe_entry.delete(0, tk.END)

# Criar janela principal
root = tk.Tk()
root.title("Lista de Convidados")

# Campos de entrada
tk.Label(root, text="Nome:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
nome_entry = tk.Entry(root, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="E-mail:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Palavra-passe:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
palavra_passe_entry = tk.Entry(root, show="*", width=30)
palavra_passe_entry.grid(row=2, column=1, padx=5, pady=5)

# Botões
adicionar_btn = tk.Button(root, text="Adicionar", command=adicionar_convidado)
adicionar_btn.grid(row=3, column=0, pady=10)

remover_btn = tk.Button(root, text="Remover", command=remover_convidado)
remover_btn.grid(row=3, column=1, pady=10)

# Lista de convidados
lista_convidados = tk.Listbox(root, width=50, height=15)
lista_convidados.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Iniciar a tabela e listar convidados
criar_tabela()
listar_convidados()

# Iniciar a aplicação
root.mainloop()
