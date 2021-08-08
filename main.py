import tkinter as tk

import src.frames as frm
import src.preload as pl


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Toovico")
        self.minsize(220, 200)
        pl.load_styles(self)

        self.ui = frm.MainUI(self)
        self.ui.notebook.add(frm.ConvertVideoTab(self), text="Convert video")
        self.ui.notebook.add(frm.ImageToVideoTab(self), text="Create video")


if __name__ == '__main__':
    app = Application()
    app.mainloop()
