import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, Menu, Frame, Button

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad with Toolbars")
        self.root.geometry("600x400")

        # Create a Text widget for the notepad area
        self.text_area = tk.Text(self.root, wrap='word', bg='white', fg='black', undo=True)
        self.text_area.pack(expand=True, fill='both')

        # Create a Menu bar
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Add File menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Add menu items
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        # Create a toolbar frame
        self.toolbar = Frame(self.root)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Add buttons to the toolbar
        Button(self.toolbar, text="New", command=self.new_file).pack(side=tk.LEFT, padx=2, pady=2)
        Button(self.toolbar, text="Open", command=self.open_file).pack(side=tk.LEFT, padx=2, pady=2)
        Button(self.toolbar, text="Save", command=self.save_file).pack(side=tk.LEFT, padx=2, pady=2)
        
        Button(self.toolbar, text="Cut", command=self.cut_text).pack(side=tk.LEFT, padx=2, pady=2)
        Button(self.toolbar, text="Copy", command=self.copy_text).pack(side=tk.LEFT, padx=2, pady=2)
        Button(self.toolbar, text="Paste", command=self.paste_text).pack(side=tk.LEFT, padx=2, pady=2)
        # Add Color menu
        self.color_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Color", menu=self.color_menu)
        
        # Add color options
        self.color_menu.add_command(label="Change Background Color", command=self.change_bg_color)


    def new_file(self):
        """Create a new file."""
        if messagebox.askokcancel("Warning", "Do you want to discard your current work?"):
            self.text_area.delete(1.0, tk.END)
            self.root.title("Notepad - Untitled")

    def open_file(self):
        """Open an existing file."""
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"),
                                                           ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)  # Clear the current text area
                self.text_area.insert(tk.END, content)  # Insert the content of the file
                self.root.title(f"Notepad - {file_path}")

    def save_file(self):
        """Save the current file."""
        try:
            if hasattr(self, 'current_file'):
                with open(self.current_file, 'w') as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
            else:
                self.save_as_file()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the file: {e}")

    def save_as_file(self):
        """Save the current content as a new file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
                self.current_file = file_path  # Store the current file path
                self.root.title(f"Notepad - {file_path}")

    def exit_app(self):
        """Exit the application with confirmation."""
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()

    def cut_text(self):
        """Cut selected text."""
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        """Copy selected text."""
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        """Paste text from clipboard."""
        self.text_area.event_generate("<<Paste>>")
    def change_bg_color(self):
        """Open a color chooser dialog and change the background color of the text widget."""
        color_code = colorchooser.askcolor(title="Choose Background Color")
        if color_code[1]:  # If a color was selected
            self.text_area.config(bg=color_code[1])



if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
