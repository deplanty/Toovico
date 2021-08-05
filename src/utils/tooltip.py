import tkinter as tk
from tkinter import ttk


class Tooltip:
    def __init__(self, widget:tk.Widget, text:str, delay:float=500):
        """
        Adds a tooltip to a tkinter widget.

        Args:
            widget (tk.Widget): the tkinter widget in need of a tooltip.
            text (str): the text displayed.
            delay (float, optional): the time delay before showing the tooltip in ms. Defaults to 500 ms.
        """

        self.widget = widget
        self.text = text
        self.delay = delay

        self.after_id = None
        self.tooltip = None

        self.widget.bind("<Enter>", self._on_mouse_enter_widget)
        self.widget.bind("<Leave>", self._on_mouse_leave_widget)

    # Events

    def _on_mouse_enter_widget(self, event):
        """
        Shows the tooltip after a delay when the mouse enter in the widget.

        Args:
            event (tkinter event): tkinter event.
        """

        self.after_id = self.widget.after(self.delay, self.show_tooltip)

    def _on_mouse_leave_widget(self, event):
        """
        Hide the tooltip when the mouse leaves the widget.

        Args:
            event (tkinter event): tkinter event.
        """

        if self.after_id is not None:
            self.widget.after_cancel(self.after_id)
            self.after_id = None

        if self.tooltip is not None:
            self.tooltip.destroy()

    # Methods

    def show_tooltip(self):
        self.tooltip = TooltipWindow(self.widget, self.text)


class TooltipWindow(tk.Toplevel):
    def __init__(self, master:tk.Widget, text:str):
        super().__init__(master)
        self.overrideredirect(True)
        x = master.winfo_rootx() + 1
        y = master.winfo_rooty() + master.winfo_height()
        self.geometry(f"+{x}+{y}")

        self.frame = ttk.Frame(self, style="Tooltip.TFrame")
        self.frame.pack()
        self.label = ttk.Label(self.frame, text=text, style="Tooltip.TLabel")
        self.label.pack(padx=1, pady=1)
