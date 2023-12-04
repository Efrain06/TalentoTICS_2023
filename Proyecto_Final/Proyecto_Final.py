import tkinter as tk
from viewer.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Analisis de Datos')
    root.iconbitmap('Proyecto_Final\ico1.ico')
    root.resizable(0,0)
    barra_menu(root)

    app = Frame(root= root)

    app.mainloop()

if __name__ == '__main__':
    main()