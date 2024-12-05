from cachorro import Cachorro
from gato import Gato
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Lista para armazenar os animais cadastrados
lista = []

# Função para cadastrar um animal
def cadastrar_animal():
    nome = entryNome.get()
    idade = entryIdade.get()
    tipo = varTipo.get()
    atributo = entryAtributo.get()

    if not nome or not idade or not atributo:
        messagebox.showinfo("Erro", "Todos os campos devem ser preenchidos!")
        return

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showinfo("Erro", "Idade deve ser um número!")
        return

    if tipo == "Cachorro":
        animal = Cachorro(nome, idade, atributo)
    elif tipo == "Gato":
        animal = Gato(nome, idade, atributo)
    else:
        messagebox.showinfo("Erro", "Tipo de animal inválido!")
        return

    lista.append(animal)
    messagebox.showinfo("Sucesso", f"{tipo} cadastrado com sucesso!")
    limpar_campos()
    atualizar_listbox()

# Função para atualizar a listbox na aba de lista
def atualizar_listbox():
    listbox.delete(0, tk.END)
    for animal in lista:
        listbox.insert(tk.END, animal.mostrar())

# Função para limpar os campos de entrada
def limpar_campos():
    entryNome.delete(0, tk.END)
    entryIdade.delete(0, tk.END)
    entryAtributo.delete(0, tk.END)

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Animais")
janela.geometry("500x400")

# Configuração do notebook (abas)
notebook = ttk.Notebook(janela)
notebook.pack(expand=True, fill="both")

# Aba de Cadastro
abaCadastro = ttk.Frame(notebook)
notebook.add(abaCadastro, text="Cadastro")

# Aba de Listapython3 main.py

abaLista = ttk.Frame(notebook)
notebook.add(abaLista, text="Lista")

# Widgets da aba Cadastro
tk.Label(abaCadastro, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entryNome = tk.Entry(abaCadastro)
entryNome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(abaCadastro, text="Idade:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entryIdade = tk.Entry(abaCadastro)
entryIdade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(abaCadastro, text="Tipo:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
varTipo = tk.StringVar(value="Cachorro")
tk.Radiobutton(abaCadastro, text="Cachorro", variable=varTipo, value="Cachorro").grid(row=2, column=1, sticky="w")
tk.Radiobutton(abaCadastro, text="Gato", variable=varTipo, value="Gato").grid(row=2, column=1, sticky="e")

tk.Label(abaCadastro, text="Porte/Raça:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entryAtributo = tk.Entry(abaCadastro)
entryAtributo.grid(row=3, column=1, padx=10, pady=5)

tk.Button(abaCadastro, text="Cadastrar", command=cadastrar_animal).grid(row=4, column=0, columnspan=2, pady=10)

# Widgets da aba Lista
listbox = tk.Listbox(abaLista, height=15, width=50)
listbox.pack(padx=10, pady=10)

tk.Button(abaLista, text="Atualizar", command=atualizar_listbox).pack(pady=10)
# Iniciar a aplicação
janela.mainloop()
