import tkinter as tk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height= 300)

    menu_inicio = tk.Menu(barra_menu, tearoff= 0)

    barra_menu.add_cascade(label= 'Inicio', menu= menu_inicio)
    menu_inicio.add_command(label='Cargar un Dataset')
    menu_inicio.add_command(label='Eliminar el Dataset')
    menu_inicio.add_command(label='Salir', command= root.destroy)

    barra_menu.add_cascade(label= 'Limpieza Dat')
    barra_menu.add_cascade(label= 'Analisis Dat')
    barra_menu.add_cascade(label= 'Ayuda')

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=580, height=420)
        self.root = root
        self.pack()
        self.config(bg='grey')