import glob
import os
import re
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog

from src.utils import ffmpeg

from .image_to_video_ui import ImageToVideoUI


class ImageToVideoTab(ttk.Frame):
    def __init__(self, master:tk.Widget):
        super().__init__(master)

        self.input_folder = None

        self.ui = ImageToVideoUI(self)
        self.ui.button_browse.configure(command=self._on_button_browse_pressed)
        self.ui.button_generate.configure(command=self._on_button_generate_pressed)

        # Show frames only when user has selected a folder
        self.ui.hide_frames()

    def _on_button_browse_pressed(self):
        folder = tk.filedialog.askdirectory()
        if not folder:
            return

        # Show frames with the parameters
        self.ui.show_frames()

        # Update UI with selected folder
        self.input_folder = folder
        self.ui.label_browse.configure(text=folder)

        # Try to guess the pattern of the files in the folder
        list_files = [os.path.basename(x) for x in glob.glob(os.path.join(folder, "*"))]
        filename = list_files[0]
        find = re.findall(r"(\w*?)(\d+)(\..*)", filename)
        if not find:
            return
        else:
            name_prefix, number, extension = find[0]
        # Update UI with the guessed pattern
        n = len(number)
        pattern = f"{name_prefix}%0{n}d{extension}"
        self.ui.entry_pattern_var.set(pattern)

    def _on_button_generate_pressed(self):
        output = tk.filedialog.asksaveasfilename()
        if not output:
            return

        if self.input_folder is None:
            return

        # Retrieve the parameters and generate the video
        pattern = self.ui.entry_pattern_var.get()
        framerate = self.ui.entry_framerate_var.get()
        ffmpeg.to_video(self.input_folder, pattern, output, framerate)
