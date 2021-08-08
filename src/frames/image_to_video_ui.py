import tkinter as tk
from tkinter import ttk


class ImageToVideoUI:
    def __init__(self, master:tk.Widget):

        self.frame_browse = ttk.Frame(master)
        self.frame_browse.pack(fill="x", pady=(5, 0))
        self.button_browse = ttk.Button(self.frame_browse, text="Browse...")
        self.button_browse.pack(side="left")
        self.label_browse = ttk.Label(self.frame_browse, text="...")
        self.label_browse.pack(side="left")

        self.frame_params = ttk.Frame(master)
        self.label_pattern = ttk.Label(self.frame_params, text="Pattern :")
        self.label_pattern.grid(row=0, column=0, sticky="w")
        self.entry_pattern_var = tk.StringVar(master, "")
        self.entry_pattern = ttk.Entry(self.frame_params, textvariable=self.entry_pattern_var)
        self.entry_pattern.grid(row=0, column=1, sticky="ew")
        self.label_framerate = ttk.Label(self.frame_params, text="Framerate :")
        self.label_framerate.grid(row=1, column=0, sticky="w")
        self.entry_framerate_var = tk.IntVar(master, 30)
        self.entry_framerate = ttk.Spinbox(self.frame_params, textvariable=self.entry_framerate_var, from_=1, to=124, width=4)
        self.entry_framerate.grid(row=1, column=1, sticky="w")
        self.frame_params.columnconfigure(1, weight=1)

        self.frame_generate = ttk.Frame(master)
        self.button_generate = ttk.Button(self.frame_generate, text="Generate...")
        self.button_generate.pack(side="left")
        self.progressbar = ttk.Progressbar(self.frame_generate)
        self.progressbar.pack(side="left", fill="x", expand=True)

    def show_frames(self):
        self.frame_params.pack(fill="x", pady=5)
        self.frame_generate.pack(fill="x", pady=5)

    def hide_frames(self):
        self.frame_params.pack_forget()
        self.frame_generate.pack_forget()
