import tkinter as tk
from tkinter import messagebox
from scraper import executar_bot

def exibir_janela():
    janela = tk.Tk()
    janela.title("NewsScraper")
    janela.geometry("400x300")

    def executar_scrappy():
        categoria = categoria_var.get() 
        if categoria == "":
            messagebox.showerror("erro", "selecione uma categoria.")
            return
        executar_bot(categoria)
        messagebox.showinfo("sucesso", f"as notícias da categoria '{categoria}' foram coletadas com sucesso!")
        janela.quit()

    label = tk.Label(janela, text="escolha a categoria para ver as notícias:", font=("Arial", 12))
    label.pack(pady=20)

    categorias = [
        "Assuntos em alta", 
        "Mais lidas", 
        "É fato ou fake", 
        "Destaques", 
        "Notícias da página principal", 
        "Ver todas as notícias"
    ]
    
    categoria_var = tk.StringVar(value="") 

    dropdown = tk.OptionMenu(janela, categoria_var, *categorias)
    dropdown.pack(pady=10)

    button = tk.Button(janela, text="ver Notícias", command=executar_scrappy, font=("Arial", 12))
    button.pack(pady=20)

    janela.mainloop()

if __name__ == "__main__":
    exibir_janela()
