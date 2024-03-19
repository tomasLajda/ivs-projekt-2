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
HOVER_COLOR = "#898989"
HOVER_OPERATOR = "#FF8409"

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Calcu-lajda")
        self.resizable(False, False)
        icon_path = r'Pictures\Calculator_30001.ico'
        self.iconbitmap(icon_path)

        self.totalExpression = "0"
        self.currentExpression = "0"

        self.digits = {
            7: (1, 1),
            8: (1, 2),
            9: (1, 3),
            4: (2, 1),
            5: (2, 2),
            6: (2, 3),
            1: (3, 1),
            2: (3, 2),
            3: (3, 3),
            0: (4, 2)
        }

        self.operations = {
            "/": "\u00F7",
            "*": "\u00D7",
            "-": "-",
            "+": "+"
        }

        self.brackets = {
            "(": "(",
            ")": ")"
        }

    def center_window(self, width, height, scale_factor=1.0):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int(((screen_width / 2) - (width / 2)) * scale_factor)
        y = int(((screen_height / 2) - (height / 2)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

    def create_display_frame(self):
        self.displayFrame = CTkFrame(self, width=400, height=150, fg_color=DARK_GRAY, border_width=5,
                                     border_color=GRAY, corner_radius=0)
        self.displayFrame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        total_label = CTkLabel(self.displayFrame, text=self.totalExpression, anchor="e", padx=15, pady=15,
                               font=(SMALL, 30), text_color="white")
        total_label.pack(side="top", expand=True, fill="both")

        current_label = CTkLabel(self.displayFrame, text=self.currentExpression, anchor="e", padx=15, pady=20,
                                 font=(LARGE, 50), text_color="white")
        current_label.pack(side="top", expand=True, fill="both")

    def create_button_frame(self):
        self.buttonFrame = CTkFrame(self, width=400, height=255, fg_color=GRAY, border_width=0, corner_radius=0)
        self.buttonFrame.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_digit_buttons(self):
        for digit, (row, column) in self.digits.items():
            button = CTkButton(self.buttonFrame, text=str(digit), bg_color=GRAY, fg_color=LIGHT_GRAY,
                               border_width=0, corner_radius=10, font=(LARGE, 25),
                               width=75, height=45, hover_color=GRAY)
            button.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)

    def create_operator_buttons(self):
        row = 1
        column = 4
        for operator, symbol in self.operations.items():
            button = CTkButton(self.buttonFrame, text=symbol, fg_color=ORANGE,
                               border_width=0, corner_radius=10, font=(LARGE, 25),
                               width=75, height=45, hover_color=HOVER_OPERATOR)
            button.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)
            row += 1

    def create_equals_button(self):
        equalsButton = CTkButton(self.buttonFrame, text="=", border_width=0, fg_color=ORANGE,
                                 corner_radius=10, font=(LARGE, 25),
                                 width=75, height=45, hover_color=HOVER_OPERATOR)
        equalsButton.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

    def create_decimal_button(self):
        decimalButton = CTkButton(self.buttonFrame, text=".", border_width=0, fg_color=LIGHT_GRAY,
                                  corner_radius=10, font=(LARGE, 25),
                                  width=75, height=45, hover_color=GRAY)
        decimalButton.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)

    def create_clean_button(self):
        cleanButton = CTkButton(self.buttonFrame, text="C", border_width=0, fg_color=COLOR_REST,
                                corner_radius=10, font=(LARGE, 25), width=75, height=45, hover_color=HOVER_COLOR)
        cleanButton.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)

    def create_delete_button(self):
        deleteButton = CTkButton(self.buttonFrame, text="⌫", border_width=0, fg_color=COLOR_REST,
                                 corner_radius=10, font=(LARGE, 25),
                                 width=75, height=45, hover_color=HOVER_COLOR)
        deleteButton.grid(row=0, column=4, sticky="nsew", padx=2, pady=2)

    def create_bracket_buttons(self):
        row = 0
        column = 1
        for bracket in self.brackets:
            button = CTkButton(self.buttonFrame, text=bracket, fg_color=COLOR_REST,
                               border_width=0, corner_radius=10, font=(LARGE, 25),
                               width=75, height=45, hover_color=HOVER_COLOR)
            button.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)
            column += 1

    def create_exponentiation_button(self):
        exponentiationButton = CTkButton(self.buttonFrame, text="x\u207F", border_width=0, fg_color=COLOR_REST,
                                         corner_radius=10, font=(LARGE, 25),
                                         width=75, height=45, hover_color=HOVER_COLOR)
        exponentiationButton.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    def create_root_button(self):
        rootButton = CTkButton(self.buttonFrame, text="ⁿ√x", border_width=0, fg_color=COLOR_REST,
                               corner_radius=10, font=(LARGE, 25),
                               width=75, height=45, hover_color=HOVER_COLOR)
        rootButton.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

    def create_factorial_button(self):
        factorialButton = CTkButton(self.buttonFrame, text="x!", border_width=0, fg_color=COLOR_REST,
                                    corner_radius=10, font=(LARGE, 25),
                                    width=75, height=45, hover_color=HOVER_COLOR)
        factorialButton.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

    def create_abs_button(self):
        absButton = CTkButton(self.buttonFrame, text="|x|", border_width=0, fg_color=COLOR_REST,
                              corner_radius=10, font=(LARGE, 25),
                              width=75, height=45, hover_color=HOVER_COLOR)
        absButton.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

    def create_modulo_button(self):
        moduloButton = CTkButton(self.buttonFrame, text="mod", border_width=0, fg_color=COLOR_REST,
                                 corner_radius=10, font=(LARGE, 25),
                                 width=75, height=45, hover_color=HOVER_COLOR)
        moduloButton.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

    def create_settings_button(self):
        settingsButton = CTkButton(self, text="⚙️", border_width=0, fg_color=DARK_GRAY,
                                   corner_radius=0, font=(LARGE, 15), width=15, height=15,
                                   bg_color=DARK_GRAY, hover_color=COLOR_REST)
        settingsButton.grid(row=0, column=0, sticky="nw", pady=2)

    def run(self):
        self.geometry(self.center_window(400, 405, self._get_window_scaling()))
        self.create_display_frame()
        self.create_button_frame()
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_equals_button()
        self.create_decimal_button()
        self.create_clean_button()
        self.create_delete_button()
        self.create_bracket_buttons()
        self.create_exponentiation_button()
        self.create_root_button()
        self.create_factorial_button()
        self.create_abs_button()
        self.create_modulo_button()
        self.create_settings_button()
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
