import json
import tkinter as tk
from tkinter import ttk


def load_styles(root:tk.Tk):
    """
    Loads the style in the tkinter main window.

    Args:
        root (tk.Tk): main window.
    """

    root.style = ttk.Style(root)
    with open("./resources/config/styles.json") as fid:
        styles = json.load(fid)

    for name, params in styles.items():
        root.style.configure(name, **params)
