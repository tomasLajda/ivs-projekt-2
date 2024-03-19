"""
@file calculator.py
@brief File containing GUI of calculator application.

@author
- Martin Valapka (xvalapm00)
@date March 19, 2024
"""

from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel

LIGHT_GRAY = "#979797"
DARK_GRAY = "#3D3D3D"
ORANGE = "#FFA500"
GRAY = "#808080"
COLOR_REST = "#4F4F4F"
LABEL_COLOR = "#25265E"
LARGE = "Arial 25 bold"
SMALL = "Arial 15"


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        icon_path = r'ui\Pictures\Calculator_30001.ico'
        self.iconbitmap(icon_path)

    def center_window(self, width, height, scale_factor=1.0):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int(((screen_width / 2) - (width / 2)) * scale_factor)
        y = int(((screen_height / 2) - (height / 2)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

    def run(self):
        self.geometry(self.center_window(400, 405, self._get_window_scaling()))


if __name__ == "__main__":
    app = App()
    app.run()
