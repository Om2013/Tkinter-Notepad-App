# basic_layout.py
import tkinter as tk
from tkinter import ttk, font

class Basic_Layout_Class:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")

        # ---------------- Toolbar ----------------
        self.toolbar = ttk.Frame(root)
        self.toolbar.pack(fill="x")

        self.bold_btn = tk.Button(self.toolbar, text="B", font=("Arial", 10, "bold"), width=3)
        self.bold_btn.pack(side="left", padx=2)
        self.italic_btn = tk.Button(self.toolbar, text="I", font=("Arial", 10, "italic"), width=3)
        self.italic_btn.pack(side="left", padx=2)
        self.underline_btn = tk.Button(self.toolbar, text="U", font=("Arial", 10, "underline"), width=3)
        self.underline_btn.pack(side="left", padx=2)

        self.apply_all_var = tk.IntVar()
        self.apply_all_check = tk.Checkbutton(self.toolbar, text="Apply to All", variable=self.apply_all_var)
        self.apply_all_check.pack(side="left", padx=5)

        # ---------------- Text Widget ----------------
        self.text_font = font.Font(family="Segoe UI", size=12)
        self.text = tk.Text(root, wrap="word", font=self.text_font, undo=True)
        self.text.pack(expand=True, fill="both", padx=4, pady=(0,4))

        # Text tags
        self.text.tag_configure("bold", font=("Segoe UI", 12, "bold"))
        self.text.tag_configure("italic", font=("Segoe UI", 12, "italic"))
        self.text.tag_configure("underline", font=("Segoe UI", 12, "underline"))

        # ---------------- Status Bar ----------------
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = tk.Label(root, textvariable=self.status_var, anchor="w")
        self.status_bar.pack(side="bottom", fill="x")

        