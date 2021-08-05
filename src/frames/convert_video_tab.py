import os
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk

from src.utils import ffmpeg

from .convert_video_ui import ConvertVideoUI


class ConvertVideoTab(ttk.Frame):
    def __init__(self, master:tk.Widget):
        super().__init__(master)

        self.input_file = None

        self.ui = ConvertVideoUI(self)
        self.ui.button_browse.configure(command=self._on_button_browse_pressed)
        self.ui.button_convert.configure(command=self._on_button_convert_pressed)

    def _on_button_browse_pressed(self):
        """
        Asks user to chose a file to convert.
        """

        filename = tk.filedialog.askopenfilename()
        if not filename:
            return

        # Get info from file
        self.input_file = filename
        _, ext = os.path.splitext(filename)
        ext = ext.lstrip(".")

        # Get size
        command = f"ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 {filename}"
        width, height = os.popen(command).read().rstrip().split(",")

        # Update GUI
        self.ui.value_from.configure(text=ext.upper())
        self.ui.label_browse.configure(text=filename)
        self.ui.entry_width_var.set(width)
        self.ui.entry_height_var.set(height)


    def _on_button_convert_pressed(self):
        """
        Asks user where to save the output file.
        """

        initialfile, _ = os.path.splitext(os.path.basename(self.input_file))
        initialfile += f".{self.ui.combo_to.get().lower()}"

        output_file = tk.filedialog.asksaveasfilename(
            initialfile=initialfile,
            defaultextension=f".{self.ui.combo_to.get().lower()}",
            filetypes=[("All files", "*.*")]
        )
        if not output_file:
            return

        output_size = f"{self.ui.entry_width_var.get()}x{self.ui.entry_height_var.get()}"

        # TODO: Use Thread and Queue to show process in the progressbar
        self.ui.progressbar.configure(mode="indeterminate")
        self.ui.progressbar.start()
        ffmpeg.convert(self.input_file, output_file, output_size)
        self.ui.progressbar.stop()
        self.ui.progressbar.configure(mode="determinate")
