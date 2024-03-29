"""
@file calculator.py
@brief File containing GUI of calculator application.

@author
- Martin Valapka (xvalapm00)

@date - March 19, 2024
"""
from sys import platform
from PIL import Image
from customtkinter import *

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


class ToplevelWindow(CTkToplevel):
    """
    @brief Initialization of the top-level window

    @param self: Instance of the class
    @param root: The parent widget
    @param *args: Variable length argument list
    @param **kwargs: Arbitrary keyword arguments
    """

    def __init__(self, root, *args, **kwargs):
        # TODO: REDO
        super().__init__(*args, **kwargs)
        self.geometry(f"300x300+{root.winfo_x() + 65}+{root.winfo_y() + 80}")
        self.title("Help")
        help_path = r'Pictures\questionmark1_83827.ico'
        self.iconbitmap(help_path)

        frame = CTkScrollableFrame(self)
        frame.configure(fg_color=DARK_GRAY)
        frame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.helpLabel = CTkLabel(frame, text="Usage", anchor="w", padx=5, pady=10,
                                  font=("Bahnschrift bold", 25), text_color=ORANGE)
        self.helpLabel.grid(row=0, column=0, sticky="nsew")

        subFrame = CTkFrame(frame)
        subFrame.configure(fg_color=GRAY, border_color="black", border_width=1, corner_radius=20)
        subFrame.grid(row=1, column=0, sticky="nsew", pady=10, padx=5)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        clearImagePath = r'Pictures\Clear.ico'
        clearImage = CTkImage(Image.open(clearImagePath), size=(45, 35))
        clear_label = CTkLabel(subFrame, image=clearImage, text="")
        clear_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        labelClear = CTkLabel(subFrame, text="Clears both the current and total expression",
                              font=("Bahnschrift bold", 15), text_color="white", wraplength=200)
        labelClear.grid(row=0, column=1, sticky="w", pady=10, padx=(0, 10))

        deleteImagePath = r'Pictures\Del.ico'
        deleteImage = CTkImage(Image.open(deleteImagePath), size=(45, 35))
        delete_label = CTkLabel(subFrame, image=deleteImage, text="")
        delete_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        labelErase = CTkLabel(subFrame, text="Erases the last digit/operator in the current expression",
                              font=("Bahnschrift bold", 15), text_color="white", wraplength=200)
        labelErase.grid(row=1, column=1, sticky="w", pady=10, padx=(0, 10))

        expImagePath = r'Pictures\^.ico'
        expImage = CTkImage(Image.open(expImagePath), size=(45, 35))
        exp_label = CTkLabel(subFrame, image=expImage, text="")
        exp_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        labelExp = CTkLabel(subFrame, text="Exponentiation: Base^Exponent = Product\n"
                                           "5^2 = 25",
                            font=("Bahnschrift bold", 15), text_color="white", wraplength=200)
        labelExp.grid(row=2, column=1, sticky="w", pady=10, padx=(0, 10))

        rootImagePath = r'Pictures\Root.ico'
        rootImage = CTkImage(Image.open(rootImagePath), size=(45, 35))
        root_label = CTkLabel(subFrame, image=rootImage, text="")
        root_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

        labelRoot = CTkLabel(subFrame, text="Root: ⁿ√x = Root\n"
                                            "n - degree, x - radical\n"
                                            "²√25 = 5",
                             font=("Bahnschrift bold", 15), text_color="white", wraplength=200)
        labelRoot.grid(row=3, column=1, sticky="w", pady=10, padx=(0, 10))

        factImagePath = r'Pictures\Fact.ico'
        factImage = CTkImage(Image.open(factImagePath), size=(45, 35))
        fact_label = CTkLabel(subFrame, image=factImage, text="")
        fact_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)

        labelFact = CTkLabel(subFrame, text="Factorial: Number\n"
                                            "(Num-1)\u00D7(Num-2) \u00D7 ... \u00D7 1\n"
                                            "4! = 4 \u00D7 3 \u00D7 2 \u00D7 1",
                             font=("Bahnschrift bold", 15), text_color="white", wraplength=200)
        labelFact.grid(row=4, column=1, sticky="w", pady=10, padx=(0, 10))

        absImagePath = r'Pictures\Abs.ico'
        absImage = CTkImage(Image.open(absImagePath), size=(45, 35))
        abs_label = CTkLabel(subFrame, image=absImage, text="")
        abs_label.grid(row=5, column=0, sticky="w", padx=10, pady=10)

        labelAbs = CTkLabel(subFrame, text="Absolute value: |Number|\n"
                                           "Returns the distance from 0\n"
                                           "|5| = 5 and |-5| = 5",
                            font=("Bahnschrift bold", 15), text_color="white", wraplength=200)
        labelAbs.grid(row=5, column=1, sticky="w", pady=10, padx=(0, 10))

        modImagePath = r'Pictures\Mod.ico'
        modImage = CTkImage(Image.open(modImagePath), size=(45, 35))
        mod_label = CTkLabel(subFrame, image=modImage, text="")
        mod_label.grid(row=6, column=0, sticky="w", padx=10, pady=10)

        labelMod = CTkLabel(subFrame, text="Modulo: Num % Num = R\n"
                                           "Evaluates the remainder after division"
                                           "7 % 3 = 1",
                            font=("Bahnschrift bold", 15), text_color="white", wraplength=200)
        labelMod.grid(row=6, column=1, sticky="w", pady=10, padx=(0, 10))

        if platform.startswith("win"):
            self.after(200, lambda: self.iconbitmap(help_path))


class App(CTk):
    """
    @brief Initialization of the calculator application.

    Attributes:
            buttonFrame: The frame containing the calculator buttons
            displayFrame: The frame containing the calculator display
            toplevel_window: The top-level window for help
            totalExpression: The total expression displayed on the calculator
            currentExpression: The current expression displayed on the calculator
            digits: Dictionary mapping digit keys
            operations: Dictionary mapping operator symbols
            brackets: Dictionary mapping bracket symbols
    """

    def __init__(self):
        super().__init__()
        self.currentLabel = None
        self.totalLabel = None
        self.buttonFrame = None
        self.displayFrame = None
        self.toplevel_window = None
        self.title("Calcu-lajda")
        self.resizable(False, False)
        icon_path = r'Pictures\Calculator_30001 (1).ico'
        self.iconbitmap(icon_path)

        self.totalExpression = ""
        self.currentExpression = ""

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

    def center_window(self, width, height, scalefactor=1.0):

        """
        @brief Calculates the position to center a window on the screen

        @param self: Instance of the class
        @param width: The width of the window
        @param height: The height of the window
        @param scalefactor: Optional scale factor to adjust the centering position
        @return: String representing the window geometry
        """

        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        x = int(((screenWidth / 2) - (width / 2)) * scalefactor)
        y = int(((screenHeight / 2) - (height / 2)) * scalefactor)
        return f"{width}x{height}+{x}+{y}"

    def create_display_frame(self):
        """
        @brief Create the display frame with total and current expression labels
        @param self: Instance of the class
        """

        self.displayFrame = CTkFrame(self, width=400, height=150, fg_color=DARK_GRAY, border_width=5,
                                     border_color=GRAY, corner_radius=0)
        self.displayFrame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.totalLabel = CTkLabel(self.displayFrame, text=self.totalExpression, anchor="e", padx=15, pady=20,
                                   font=(SMALL, 25), text_color="white")
        self.totalLabel.pack(side="top", expand=True, fill="both")

        self.currentLabel = CTkLabel(self.displayFrame, text=self.currentExpression, anchor="e", padx=15, pady=20,
                                     font=(LARGE, 50), text_color="white")
        self.currentLabel.pack(side="top", expand=True, fill="both")

    def update_total_label(self):
        """
        @brief Updates the total expression label
        @param self: Instance of the class
        """
        expression = self.totalExpression

        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        self.totalLabel.configure(text=expression[:25])

    def update_current_label(self):
        """
        @brief Updates the current expression label by truncating if necessary
        @param self: Instance of the class
        """
        if len(self.currentExpression) > 14:
            self.currentExpression = self.currentExpression[-14:]
        self.currentLabel.configure(text=self.currentExpression)

    def create_button_frame(self):
        """
        @brief Creates a frame for buttons in the calculator interface
        @param self: Instance of the class
        """

        self.buttonFrame = CTkFrame(self, width=400, height=255, fg_color=GRAY, border_width=0, corner_radius=0)
        self.buttonFrame.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show_numbers(self, value):
        """
        @brief Appends the provided value to the current expression and updates the current label.
        @param self: Instance of the class
        @param value: The value to append to the current expression
        """

        self.currentExpression += str(value)
        self.update_current_label()

    def create_digit_buttons(self):
        """
        @brief Creates digit buttons in the calculator interface
        @param self: Instance of the class
        """

        for digit, (row, column) in self.digits.items():
            button = CTkButton(self.buttonFrame, text=str(digit), bg_color=GRAY, fg_color=LIGHT_GRAY,
                               border_width=0, corner_radius=10, font=(LARGE, 25),
                               width=75, height=45, hover_color=GRAY, command=lambda x=digit: self.show_numbers(x))
            button.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)

    def show_operators(self, operator):
        # TODO: NEEDS FIX
        """
        @brief Appends the provided operator to the current expression and updates the labels.
        @param self: Instance of the class
        @param operator: The operator to append to the current expression
        """

        self.currentExpression += operator
        self.totalExpression += self.currentExpression
        self.currentExpression = ''
        self.update_total_label()
        self.update_current_label()

    def create_operator_buttons(self):
        """
        @brief Creates operator buttons in the calculator interface
        @param self: Instance of the class
        """

        row = 1
        column = 4
        for operator, symbol in self.operations.items():
            button = CTkButton(self.buttonFrame, text=symbol, fg_color=ORANGE,
                               border_width=0, corner_radius=10, font=(LARGE, 25),
                               width=75, height=45, hover_color=HOVER_OPERATOR,
                               command=lambda op=operator: self.show_operators(op))
            button.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)
            row += 1

    def equals(self):
        # TODO: IMPLEMENT
        pass

    def create_equals_button(self):
        """
        @brief Creates equals button in the calculator interface that evaluates the expression
        @param self: Instance of the class
        """

        equalsButton = CTkButton(self.buttonFrame, text="=", border_width=0, fg_color=ORANGE,
                                 corner_radius=10, font=(LARGE, 25),
                                 width=75, height=45, hover_color=HOVER_OPERATOR)
        equalsButton.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

    def decimal(self):
        """
        @brief Adds a decimal point to the current expression
        @param self: Instance of the class
        """

        if any(char.isdigit() for char in self.currentExpression):
            if not self.currentExpression or '.' not in self.currentExpression:
                self.currentExpression += '.'
                self.update_current_label()

    def create_decimal_button(self):
        """
        @brief Creates decimal point button in the calculator interface
        @param self: Instance of the class
        """

        decimalButton = CTkButton(self.buttonFrame, text=".", border_width=0, fg_color=LIGHT_GRAY,
                                  corner_radius=10, font=(LARGE, 25),
                                  width=75, height=45, hover_color=GRAY,
                                  command=self.decimal)
        decimalButton.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)

    def clear(self):
        """
        @brief Clears both the current and totol expression
        @param self: Instance of the class
        """

        self.currentExpression = ""
        self.totalExpression = ""
        self.update_total_label()
        self.update_current_label()

    def create_clean_button(self):
        """
        @brief Creates Clean button in the calculator interface that clears the expression
        @param self: Instance of the class
        """

        cleanButton = CTkButton(self.buttonFrame, text="C", border_width=0, fg_color=COLOR_REST,
                                corner_radius=10, font=(LARGE, 25), width=75, height=45, hover_color=HOVER_COLOR,
                                command=self.clear)
        cleanButton.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)

    def delete(self):
        """
        @brief Deletes the last character from the current expression
        @param self: Instance of the class
        """

        if self.currentExpression:
            self.currentExpression = self.currentExpression[:-1]
            self.update_current_label()

    def create_delete_button(self):
        """
        @brief Creates Delete button in the calculator interface that erases the last character
        @param self: Instance of the class
        """

        deleteButton = CTkButton(self.buttonFrame, text="⌫", border_width=0, fg_color=COLOR_REST,
                                 corner_radius=10, font=(LARGE, 25),
                                 width=75, height=45, hover_color=HOVER_COLOR, command=self.delete)
        deleteButton.grid(row=0, column=4, sticky="nsew", padx=2, pady=2)

    def show_brackets(self, bracket):
        """
        @brief Appends the selected bracket to the current expression and updates the display label
        @param self: Instance of the class
        @param bracket: The bracket symbol to be added
        """

        self.currentExpression += self.brackets[bracket]
        self.update_current_label()

    def create_bracket_buttons(self):
        """
        @brief Creates bracket buttons in the calculator interface
        @param self: Instance of the class
        """

        row = 0
        column = 1
        for bracket in self.brackets:
            button = CTkButton(self.buttonFrame, text=bracket, fg_color=COLOR_REST,
                               border_width=0, corner_radius=10, font=(LARGE, 25),
                               width=75, height=45, hover_color=HOVER_COLOR,
                               command=lambda b=bracket: self.show_brackets(b))
            button.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)
            column += 1

    def exponentiation(self):
        # TODO: IMPLEMENT
        pass

    def create_exponentiation_button(self):
        """
        @brief Creates exponentiation button in the calculator interface
        @param self: Instance of the class
        """

        exponentiationButton = CTkButton(self.buttonFrame, text="x\u207F", border_width=0, fg_color=COLOR_REST,
                                         corner_radius=10, font=(LARGE, 25),
                                         width=75, height=45, hover_color=HOVER_COLOR)
        exponentiationButton.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    def root(self):
        # TODO: IMPLEMENT
        pass

    def create_root_button(self):
        """
        @brief Creates root button in the calculator interface
        @param self: Instance of the class
        """

        rootButton = CTkButton(self.buttonFrame, text="ⁿ√x", border_width=0, fg_color=COLOR_REST,
                               corner_radius=10, font=(LARGE, 25),
                               width=75, height=45, hover_color=HOVER_COLOR)
        rootButton.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

    def factorial(self):
        # TODO: IMPLEMENT
        pass

    def create_factorial_button(self):
        """
        @brief Creates factorial button in the calculator interface
        @param self: Instance of the class
        """

        factorialButton = CTkButton(self.buttonFrame, text="x!", border_width=0, fg_color=COLOR_REST,
                                    corner_radius=10, font=(LARGE, 25),
                                    width=75, height=45, hover_color=HOVER_COLOR)
        factorialButton.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

    def abs(self):
        # TODO: IMPLEMENT
        pass

    def create_abs_button(self):
        """
        @brief Creates button in the calculator interface for the absolute value of the expression
        @param self: Instance of the class
        """

        absButton = CTkButton(self.buttonFrame, text="|x|", border_width=0, fg_color=COLOR_REST,
                              corner_radius=10, font=(LARGE, 25),
                              width=75, height=45, hover_color=HOVER_COLOR)
        absButton.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

    def modulo(self):
        # TODO: IMPLEMENT
        pass

    def create_modulo_button(self):
        """
        @brief Creates button in the calculator interface for the modulo operation
        @param self: Instance of the class
        """

        moduloButton = CTkButton(self.buttonFrame, text="mod", border_width=0, fg_color=COLOR_REST,
                                 corner_radius=10, font=(LARGE, 25),
                                 width=75, height=45, hover_color=HOVER_COLOR)
        moduloButton.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

    def create_settings_button(self):
        """
        @brief Creates a settings/help button in the calculator interface
        @param self: Instance of the class
        """

        settingsImagePath = r'Pictures\Vrstva 1.ico'
        settingsImage = CTkImage(Image.open(settingsImagePath))
        settingsButton = CTkButton(self, image=settingsImage, text="", border_width=0, fg_color=DARK_GRAY,
                                   corner_radius=25, font=(LARGE, 15), width=10, height=10,
                                   bg_color=DARK_GRAY, hover_color=COLOR_REST, command=self.open_settings_window)
        settingsButton.grid(row=0, column=0, sticky="nw", pady=2)

    def open_settings_window(self):
        """
        @brief Opens the settings window.

        If the settings window is not open, it creates a new one and links it to the root window.
        Otherwise, it just focuses on the existing window.

        @param self: Instance of the class
        """

        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
            self.toplevel_window.wm_transient(self)
        else:
            self.toplevel_window.focus()

    def bind_keys(self):
        # TODO: MISSING KEYS
        """
        @brief Binds keyboard keys to calculator operations and digits
        @param self: Instance of the class
        """

        for key in self.digits:
            self.bind(str(key), lambda event, digit=key: self.show_numbers(digit))

        for key in self.operations:
            self.bind(str(key), lambda event, op=key: self.show_operators(op))

        for key in self.brackets:
            self.bind(str(key), lambda event, bracket=key: self.show_brackets(bracket))

        self.bind("<BackSpace>", lambda event: self.delete())
        self.bind("<c>", lambda event: self.clear())
        self.bind("<.>", lambda event: self.decimal())

    def run(self):
        """
        @brief Runs the application.
        @param self: Instance of the class
        """

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
        self.bind_keys()
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
