import tkinter as tk
from tkinter import messagebox
import gerenciador

class MindClearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MindClear - Organizador de Rotina")
        self.root.geometry("400x500")
        
        # Título
        tk.Label(root, text="Descarregue sua mente", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        # Campo de entrada
        self.entrada_tarefa = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.entrada_tarefa.pack(pady=10)
        
        # Botão Adicionar
        tk.Button(root, text="Adicionar Tarefa", command=self.adicionar, bg="#4CAF50", fg="white").pack(pady=5)
        
        # Lista de Tarefas
        self.lista_box = tk.Listbox(root, font=("Helvetica", 12), width=40, height=15)
        self.lista_box.pack(pady=10)
        
        # Botão Concluir
        tk.Button(root, text="Marcar como Concluída", command=self.concluir, bg="#2196F3", fg="white").pack(pady=5)
        
        self.atualizar_lista()

    def adicionar(self):

        descricao = self.entrada_tarefa.get()
        try:
            gerenciador.adicionar_tarefa(descricao)
            self.entrada_tarefa.delete(0, tk.END)
            self.atualizar_lista()
        except ValueError as e:
            messagebox.showwarning("Aviso", str(e))

    def concluir(self):
        selecao = self.lista_box.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir.")
            return
            
        texto_selecionado = self.lista_box.get(selecao[0])
        # Pega o ID que está no início do texto (ex: "1 - Comprar pão")
        id_tarefa = int(texto_selecionado.split(" - ")[0])
        
        gerenciador.concluir_tarefa(id_tarefa)
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_box.delete(0, tk.END)
        tarefas = gerenciador.listar_tarefas()
        for t in tarefas:
            status = "✓" if t["concluida"] else "O"
            texto = f"{t['id']} - [{status}] {t['descricao']}"
            self.lista_box.insert(tk.END, texto)
            # Pinta de cinza se estiver concluída
            if t["concluida"]:
                self.lista_box.itemconfig(tk.END, {'fg': 'gray'})

if __name__ == "__main__":
    root = tk.Tk()
    app = MindClearApp(root)
    root.mainloop()