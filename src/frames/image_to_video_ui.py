import tkinter as tk
from tkinter import ttk


class ImageToVideoUI:
    def __init__(self, master:tk.Widget):

        self.button_browse = ttk.Button(master, text="Browse...")
        self.button_browse.pack()
