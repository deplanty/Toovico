import os
import shutil
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog

from .image_to_video_ui import ImageToVideoUI


class ImageToVideoTab(ttk.Frame):
    def __init__(self, master:tk.Widget):
        super().__init__(master)

        self.ui = ImageToVideoUI(self)
        self.ui.button_browse.configure(command=self._on_button_browse_pressed)

    def _on_button_browse_pressed(self):
        filenames = tk.filedialog.askopenfilenames()
        if not filenames:
            return

        self.list_images = filenames
        _, extension = os.path.splitext(filenames[0])

        working_dir = os.path.dirname(filenames[0])
        tmp_dir = os.path.join(working_dir, "tmp")
        os.makedirs(tmp_dir, exist_ok=True)
        for i, file in enumerate(filenames):
            frame = f"frame_{i:05d}{extension}"
            shutil.copy(file, os.path.join(tmp_dir, frame))

        output = os.path.join(working_dir, "output.mp4")
        input = os.path.join(tmp_dir, f"frame_%05d{extension}")
        command = f"ffmpeg -framerate 30 -y -i {input} {output}"
        os.system(command)
