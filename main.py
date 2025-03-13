import tkinter as tk
from tkinter import messagebox

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Editor de Texto")
        master.geometry("800x600")

        self.text_area = tk.Text(master, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill='both')
        
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)
        
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Abrir (Ctrl+O)", command=self.open_file)
        file_menu.add_command(label="Guardar (Ctrl+S)", command=self.save_file)
        file_menu.add_command(label="Borrar (Ctrl+N)", command=self.clear_text)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=master.quit)

        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Cambiar Color", command=self.change_color)
        edit_menu.add_command(label="Buscar y Reemplazar", command=self.find_replace)

        master.bind('<Control-o>', lambda event: self.open_file())
        master.bind('<Control-s>', lambda event: self.save_file())
        master.bind('<Control-n>', lambda event: self.clear_text())

    def open_file(self):
        messagebox.showinfo("Abrir", "Función para abrir archivo (no implementada)")

    def save_file(self):
        messagebox.showinfo("Guardar", "Función para guardar archivo (no implementada)")

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)

    def change_color(self):
        messagebox.showinfo("Cambiar Color", "Función para cambiar color (no implementada)")

    def find_replace(self):
        messagebox.showinfo("Buscar y Reemplazar", "Función para buscar y reemplazar (no implementada)")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
