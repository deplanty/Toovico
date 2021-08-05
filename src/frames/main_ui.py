import tkinter as tk
from tkinter import ttk


class MainUI:
    def __init__(self, master:tk.Widget):

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill="both", expand=True)
