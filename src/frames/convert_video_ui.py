import tkinter as tk
from tkinter import ttk


class ConvertVideoUI:
    def __init__(self, master:tk.Widget):

        self.frame_browse = ttk.Frame(master)
        self.frame_browse.grid(row=0, pady=5, sticky="w")
        self.button_browse = ttk.Button(self.frame_browse, text="Browse...")
        self.button_browse.pack(side="left")
        self.label_browse = ttk.Label(self.frame_browse, text="")
        self.label_browse.pack(side="left")

        self.frame_params = ttk.Frame(master)
        self.frame_params.grid(row=1, pady=(0, 5), sticky="w")
        self.label_from = ttk.Label(self.frame_params, text="From")
        self.label_from.pack(side="left")
        self.value_from = ttk.Label(self.frame_params, text="PNG", style="Entry.TLabel")
        self.value_from.pack(side="left")
        self.label_to = ttk.Label(self.frame_params, text="to")
        self.label_to.pack(side="left")
        self.combo_to = ttk.Combobox(self.frame_params)
        self.combo_to.pack(side="left")
