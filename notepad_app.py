import os
import tkinter as tk
from tkinter import StringVar, filedialog, messagebox
from basic_layout import Basic_Layout_Class
from helpers import Helpers_Class
from sounds import Sounds_Class

# ---------------- Main App ----------------
root = tk.Tk()
root.title("My Notepad")
root.geometry("800x600")

# ---------------- Sounds ----------------
try:
    sounds = Sounds_Class()
except Exception:
    sounds = None

# ---------------- Layout ----------------
layout = Basic_Layout_Class(root)
text = layout.text
status_var = layout.status_var

# ---------------- Functions ----------------
functions = Helpers_Class(root, text, current_file=None, sounds=sounds, status_var=status_var)
layout.helpers = functions  # attach helpers to layout

# ---------------- Toolbar Buttons ----------------
def apply_style(style):
    functions.toggle_style(style, apply_to_all=bool(layout.apply_all_var.get()))

layout.bold_btn.config(command=lambda: apply_style('bold'))
layout.italic_btn.config(command=lambda: apply_style('italic'))
layout.underline_btn.config(command=lambda: apply_style('underline'))

# ---------------- Menu ----------------
menubar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=functions.new_file)
file_menu.add_command(label="Open", command=functions.open_file)
file_menu.add_command(label="Save", command=functions.save_file)
file_menu.add_command(label="Save As...", command=functions.save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=functions.quit_app)
menubar.add_cascade(label="File", menu=file_menu)

# Help Menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Help", command=lambda: messagebox.showinfo("Help", "Notepad clone with formatting and CSV export!"))
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

# ---------------- Run App ----------------
root.mainloop()
