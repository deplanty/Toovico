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
        self.value_from = ttk.Label(self.frame_params, text="...", style="Entry.TLabel")
        self.value_from.pack(side="left")
        self.label_to = ttk.Label(self.frame_params, text="to")
        self.label_to.pack(side="left")
        self.combo_to = ttk.Combobox(self.frame_params)
        self.combo_to.pack(side="left")

        self.frame_size = ttk.Frame(master)
        self.frame_size.grid(row=2, pady=(0, 5), sticky="w")
        self.label_output_size = ttk.Label(self.frame_size, text="Output size")
        self.label_output_size.pack(side="left")
        self.entry_width_var = tk.StringVar(master, "")
        self.entry_width = ttk.Entry(self.frame_size, textvariable=self.entry_width_var)
        self.entry_width.pack(side="left")
        self.label_x = ttk.Label(self.frame_size, text="x")
        self.label_x.pack(side="left")
        self.entry_height_var = tk.StringVar(master, "")
        self.entry_height = ttk.Entry(self.frame_size, textvariable=self.entry_height_var)
        self.entry_height.pack(side="left")

        self.frame_convert = ttk.Frame(master)
        self.frame_convert.grid(row=3, pady=(0, 5), sticky="we")
        self.button_convert = ttk.Button(self.frame_convert, text="Convert")
        self.button_convert.pack(side="left")
        self.progressbar = ttk.Progressbar(self.frame_convert)
        self.progressbar.pack(side="left", fill="x", expand=True)
