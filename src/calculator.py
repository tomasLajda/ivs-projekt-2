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
        icon_path = r'Pictures\Calculator_30001.ico'
        self.iconbitmap(icon_path)

        self.totalExpression = "0"
        self.currentExpression = "0"

    def center_window(self, width, height, scale_factor=1.0):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int(((screen_width / 2) - (width / 2)) * scale_factor)
        y = int(((screen_height / 2) - (height / 2)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

    def create_display_frame(self):
        self.displayFrame = CTkFrame(self, width=400, height=150, fg_color=DARK_GRAY, border_width=5, corner_radius=0)
        self.displayFrame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)

        total_label = CTkLabel(self.displayFrame, text=self.totalExpression, anchor="e", padx=15, pady=15, font=(SMALL, 30))
        total_label.pack(side="top", expand=True, fill="both")

        current_label = CTkLabel(self.displayFrame, text=self.currentExpression, anchor="e", padx=15, pady=20, font=(LARGE, 50))
        current_label.pack(side="top", expand=True, fill="both")

    def create_button_frame(self):
        self.buttonFrame = CTkFrame(self, width=400, height=255, fg_color=GRAY, border_width=0, corner_radius=0)
        self.buttonFrame.grid(row=1, column=0, sticky="nsew", rowspan=2)
        self.grid_rowconfigure(1, weight=1)

    def run(self):
        self.geometry(self.center_window(400, 405, self._get_window_scaling()))
        self.create_display_frame()
        self.create_button_frame()
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
