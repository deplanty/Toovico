import tkinter as tk
from tkinter import ttk

from .convert_video_ui import ConvertVideoUI


class ConvertVideoTab(ttk.Frame):
    def __init__(self, master:tk.Widget):
        super().__init__(master)

        self.ui = ConvertVideoUI(self)
