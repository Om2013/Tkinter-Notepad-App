# helpers.py
import os
import tkinter as tk
from tkinter import filedialog, messagebox, font

class Helpers_Class:
    def __init__(self, root, text, current_file=None, sounds=None, status_var=None):
        self.root = root
        self.text = text
        self.sounds = sounds
        self.status_var = status_var
        self.current_file = current_file

        # ---------------- Shortcuts ----------------
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-Shift-S>', lambda e: self.save_as_file())
        self.root.bind('<Control-q>', lambda e: self.quit_app())

        # ---------------- Font Styles ----------------
        try:
            font_info = font.Font(font=self.text['font']).actual()
        except tk.TclError:
            font_info = font.Font(family="Arial", size=12).actual()

        self.bold_font = font.Font(**font_info)
        self.bold_font.configure(weight='bold')

        self.italic_font = font.Font(**font_info)
        self.italic_font.configure(slant='italic')

        self.underline_font = font.Font(**font_info)
        self.underline_font.configure(underline=True)

        # ---------------- Tags ----------------
        self.text.tag_configure("bold", font=self.bold_font)
        self.text.tag_configure("italic", font=self.italic_font)
        self.text.tag_configure("underline", font=self.underline_font)

    # ---------------- File Functions ----------------
    def new_file(self):
        if self.text.get('1.0', 'end-1c').strip():
            if not messagebox.askyesno("Confirm", "Unsaved changes will be lost. Continue?"):
                return
        self.text.delete('1.0', 'end')
        self.current_file = None
        if self.status_var:
            self.status_var.set("New file created")
        if self.sounds:
            self.sounds.play('new')

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text.delete('1.0', 'end')
                self.text.insert('1.0', content)
                self.current_file = file_path
                if self.status_var:
                    self.status_var.set(f"Opened: {os.path.basename(file_path)}")
                if self.sounds:
                    self.sounds.play('open')
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{e}")

    def save_file(self):
        if self.current_file:
            self._write_file(self.current_file)
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.current_file = file_path
            self._write_file(file_path)

    def _write_file(self, file_path):
        try:
            content = self.text.get('1.0', 'end-1c')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            if self.status_var:
                self.status_var.set(f"Saved: {os.path.basename(file_path)}")
            if self.sounds:
                self.sounds.play('save')
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")

    def quit_app(self):
        if self.text.get('1.0', 'end-1c').strip():
            if not messagebox.askyesno("Confirm", "Unsaved changes will be lost. Quit?"):
                return
        self.root.destroy()

    # ---------------- Formatting Functions ----------------
    def toggle_style(self, style, apply_to_all=False):
        if apply_to_all:
            start = '1.0'
            end = 'end'
        else:
            try:
                start = self.text.index("sel.first")
                end = self.text.index("sel.last")
            except tk.TclError:
                return  # no selection

        # Toggle style
        ranges = self.text.tag_ranges(style)
        fully_applied = False
        if ranges:
            fully_applied = self.text.tag_nextrange(style, start, end) == (start, end)

        if fully_applied:
            self.text.tag_remove(style, start, end)
        else:
            self.text.tag_add(style, start, end)

        if not apply_to_all:
            self.text.tag_add("sel", start, end)
