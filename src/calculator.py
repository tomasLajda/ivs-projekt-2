"""
@file calculator.py
@brief File containing GUI of calculator application.

@author
- Martin Valapka (xvalapm00)

@date - March 19, 2024
"""

import mathlib
import platform
from help_menu import ToplevelWindow
from PIL import Image, ImageTk
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


def adjust_button_size(width, height):
    """
    @brief Adjusts the button size based on the platform
    @param width: Original button width
    @param height: Original button height
    @return: Adjusted button width and height
    """
    if platform.system() == 'Linux':
        width += 15
        height += 15
    return width, height


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
        self.numbers = None
        self.settingsImagePath = None
        self.currentLabel = None
        self.totalLabel = None
        self.buttonFrame = None
        self.displayFrame = None
        self.toplevel_window = None
        self.title("Calcu-lajda")
        self.resizable(False, False)

        if platform.system() == "Linux":
            self.iconpath = ImageTk.PhotoImage(file=os.path.join("Pictures", "Calculator_30001 (1)-1.png"))
            self.wm_iconbitmap()
            self.iconphoto(False, self.iconpath)

        self.iconbitmap("Pictures/Calculator_30001 (1).ico")

        self.totalExpression = ""
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

        self.precedences = {
            "+": (1, 2),
            "-": (1, 2),
            "*": (3, 4),
            "/": (3, 4)
        }

        self.Integer = "Integer"
        self.Operator = "Operator"
        self.Paren = "Parenthesis"
        self.EOF = "EOF"

        self.functions = {
            "+": lambda a, b: mathlib.add(a, b),
            "-": lambda a, b: mathlib.sub(a, b),
            "\u00D7": lambda a, b: mathlib.mul(a, b),
            "\u00F7": lambda a, b: mathlib.div(a, b)
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
        os_name = platform.system()
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        if os_name == 'Linux':
            x = int(((screenWidth / 2) - (width / 2)) * scalefactor)
            y = int(((screenHeight / 2) - (height / 2)) * scalefactor)
            return f"{width + 75}x{height + 80}+{x}+{y}"

        else:
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
        self.totalLabel.grid(row=0, column=0, sticky="nsew")

        self.currentLabel = CTkLabel(self.displayFrame, text=self.currentExpression, anchor="e", padx=15, pady=20,
                                     font=(LARGE, 50), text_color="white")
        self.currentLabel.grid(row=1, column=0, sticky="nsew")

        self.displayFrame.grid_rowconfigure(0, weight=1)
        self.displayFrame.grid_rowconfigure(1, weight=1)
        self.displayFrame.grid_columnconfigure(0, weight=1)

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
        if self.currentExpression.startswith("0"):
            self.currentExpression = self.currentExpression[1:]

        if len(self.currentExpression) > 14:
            self.currentExpression = self.currentExpression[:14]

        # If currentExpression is empty or "0", display "0"
        if not self.currentExpression or self.currentExpression == "0":
            self.currentLabel.configure(text="0")
        else:
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
        button_width, button_height = adjust_button_size(75, 45)
        for digit, (row, column) in self.digits.items():
            button = CTkButton(self.buttonFrame, text=str(digit), bg_color=GRAY, fg_color=LIGHT_GRAY,
                               border_width=0, corner_radius=10, font=(LARGE, 25),
                               width=button_width, height=button_height, hover_color=GRAY,
                               command=lambda x=digit: self.show_numbers(x))
            button.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)
            self.buttonFrame.grid_rowconfigure(row, weight=1)  # Allow row to expand
            self.buttonFrame.grid_columnconfigure(column, weight=1)  # Allow column to expand

    def add(self):
        """
        @brief Adds two numbers
        @param self: Instance of the class
        """
        result = mathlib.add(float(self.totalExpression), float(self.currentExpression))
        result = int(result)
        self.totalExpression = str(self.totalExpression) + '+' + str(self.currentExpression)
        self.update_total_label()
        self.currentExpression = str(result)
        self.update_current_label()

    def show_operators(self, operator):
        """
        @brief Appends the provided operator to the current expression and updates the labels.
        @param self: Instance of the class
        @param operator: The operator to append to the current expression
        """
        # TODO NEEDS FIXES WITH FIRST CHAR AS AN OPERATOR

        if (self.totalExpression and self.totalExpression[-1] in "+-*/" and not self.currentExpression and
                len(self.totalExpression) != 0):
            self.totalExpression = self.totalExpression[:-1] + operator
        else:
            self.totalExpression += self.currentExpression + operator

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
        button_width, button_height = adjust_button_size(75, 45)
        for operator, symbol in self.operations.items():
            button = CTkButton(self.buttonFrame, text=symbol, fg_color=ORANGE,
                               border_width=0, corner_radius=10, font=(LARGE, 25),
                               width=button_width, height=button_height, hover_color=HOVER_OPERATOR,
                               command=lambda op=operator: self.show_operators(op))
            button.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)
            self.buttonFrame.grid_rowconfigure(row, weight=1)
            self.buttonFrame.grid_columnconfigure(column, weight=1)
            row += 1

    def equals(self):
        # TODO: IMPLEMENT
        self.totalExpression = self.totalExpression[:-1]
        self.add()

    def create_equals_button(self):
        """
        @brief Creates equals button in the calculator interface that evaluates the expression
        @param self: Instance of the class
        """
        button_width, button_height = adjust_button_size(75, 45)
        equalsButton = CTkButton(self.buttonFrame, text="=", border_width=0, fg_color=ORANGE,
                                 corner_radius=10, font=(LARGE, 25),
                                 width=button_width, height=button_height, hover_color=HOVER_OPERATOR,
                                 command=self.equals)
        equalsButton.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)
        self.buttonFrame.grid_rowconfigure(4, weight=1)
        self.buttonFrame.grid_columnconfigure(3, weight=1)

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
        button_width, button_height = adjust_button_size(75, 45)
        decimalButton = CTkButton(self.buttonFrame, text=".", border_width=0, fg_color=LIGHT_GRAY,
                                  corner_radius=10, font=(LARGE, 25),
                                  width=button_width, height=button_height, hover_color=GRAY,
                                  command=self.decimal)
        decimalButton.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
        self.buttonFrame.grid_rowconfigure(4, weight=1)
        self.buttonFrame.grid_columnconfigure(1, weight=1)

    def clear(self):
        """
        @brief Clears both the current and total expression
        @param self: Instance of the class
        """

        self.currentExpression = "0"
        self.totalExpression = ""
        self.update_total_label()

        if not self.currentExpression:
            self.currentExpression = "0"

        self.update_current_label()

    def create_clean_button(self):
        """
        @brief Creates Clean button in the calculator interface that clears the expression
        @param self: Instance of the class
        """
        button_width, button_height = adjust_button_size(75, 45)
        cleanButton = CTkButton(self.buttonFrame, text="C", border_width=0, fg_color=COLOR_REST,
                                corner_radius=10, font=(LARGE, 25), width=button_width, height=button_height,
                                hover_color=HOVER_COLOR, command=self.clear)
        cleanButton.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)
        self.buttonFrame.grid_rowconfigure(0, weight=1)  # Allow row to expand
        self.buttonFrame.grid_columnconfigure(3, weight=1)  # Allow column to expand

    def delete(self):
        """
        @brief Deletes the last character from the current expression
        @param self: Instance of the class
        """

        if self.currentExpression:
            self.currentExpression = self.currentExpression[:-1]
            self.update_current_label()

        if len(self.currentExpression) == 0:
            self.currentExpression = "0"
            self.update_current_label()

    def create_delete_button(self):
        """
        @brief Creates Delete button in the calculator interface that erases the last character
        @param self: Instance of the class
        """
        button_width, button_height = adjust_button_size(75, 45)
        deleteButton = CTkButton(self.buttonFrame, text="⌫", border_width=0, fg_color=COLOR_REST,
                                 corner_radius=10, font=(LARGE, 25),
                                 width=button_width, height=button_height, hover_color=HOVER_COLOR,
                                 command=self.delete)
        deleteButton.grid(row=0, column=4, sticky="nsew", padx=2, pady=2)
        self.buttonFrame.grid_rowconfigure(0, weight=1)  # Allow row to expand
        self.buttonFrame.grid_columnconfigure(4, weight=1)  # Allow column to expand

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
        button_width, button_height = adjust_button_size(75, 45)
        row = 0
        column = 1
        for bracket in self.brackets:
            button = CTkButton(self.buttonFrame, text=bracket, fg_color=COLOR_REST,
                               border_width=0, corner_radius=10, font=(LARGE, 25),
                               width=button_width, height=button_height, hover_color=HOVER_COLOR,
                               command=lambda b=bracket: self.show_brackets(b))
            button.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)
            column += 1
        self.buttonFrame.grid_rowconfigure(row, weight=1)
        self.buttonFrame.grid_columnconfigure(column - 1, weight=1)

    def exponentiation(self):
        # TODO: IMPLEMENT
        pass

    def create_exponentiation_button(self):
        """
        @brief Creates exponentiation button in the calculator interface
        @param self: Instance of the class
        """

        button_width, button_height = adjust_button_size(75, 45)
        exponentiationButton = CTkButton(self.buttonFrame, text="x\u207F", border_width=0, fg_color=COLOR_REST,
                                         corner_radius=10, font=(LARGE, 25),
                                         width=button_width, height=button_height, hover_color=HOVER_COLOR)
        exponentiationButton.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.buttonFrame.grid_rowconfigure(0, weight=1)
        self.buttonFrame.grid_columnconfigure(0, weight=1)

    def root(self):
        # TODO: IMPLEMENT
        pass

    def create_root_button(self):
        """
        @brief Creates root button in the calculator interface
        @param self: Instance of the class
        """

        button_width, button_height = adjust_button_size(75, 45)
        rootButton = CTkButton(self.buttonFrame, text="ⁿ√x", border_width=0, fg_color=COLOR_REST,
                               corner_radius=10, font=(LARGE, 25),
                               width=button_width, height=button_height, hover_color=HOVER_COLOR)
        rootButton.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        self.buttonFrame.grid_rowconfigure(1, weight=1)
        self.buttonFrame.grid_columnconfigure(0, weight=1)

    def factorial(self):
        """
        @brief Computes the factorial of the current expression
        @param self: Instance of the class
        """
        # TODO: IMPLEMENT
        result = mathlib.fac(int(self.currentExpression))
        self.totalExpression = str(self.currentExpression) + '!'
        self.update_total_label()
        self.currentExpression = str(result)
        self.update_current_label()

    def create_factorial_button(self):
        """
        @brief Creates factorial button in the calculator interface
        @param self: Instance of the class
        """

        button_width, button_height = adjust_button_size(75, 45)
        factorialButton = CTkButton(self.buttonFrame, text="x!", border_width=0, fg_color=COLOR_REST,
                                    corner_radius=10, font=(LARGE, 25),
                                    width=button_width, height=button_height, hover_color=HOVER_COLOR,
                                    command=self.factorial)
        factorialButton.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        self.buttonFrame.grid_rowconfigure(2, weight=1)
        self.buttonFrame.grid_columnconfigure(0, weight=1)

    def abs(self):
        """
        @brief Computes the absolute value of the current expression
        @param self: Instance of the class
        """
        # TODO: IMPLEMENT
        if '.' in self.currentExpression:
            result = mathlib.abs(float(self.currentExpression))
        else:
            result = mathlib.abs(int(self.currentExpression))

        self.totalExpression = '|' + str(self.currentExpression) + '|'
        self.update_total_label()
        self.currentExpression = str(result)
        self.update_current_label()

    def create_abs_button(self):
        """
        @brief Creates button in the calculator interface for the absolute value of the expression
        @param self: Instance of the class
        """

        button_width, button_height = adjust_button_size(75, 45)
        absButton = CTkButton(self.buttonFrame, text="|x|", border_width=0, fg_color=COLOR_REST,
                              corner_radius=10, font=(LARGE, 25),
                              width=button_width, height=button_height, hover_color=HOVER_COLOR, command=self.abs)
        absButton.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
        self.buttonFrame.grid_rowconfigure(3, weight=1)
        self.buttonFrame.grid_columnconfigure(0, weight=1)

    def modulo(self):
        # TODO: IMPLEMENT
        pass

    def create_modulo_button(self):
        """
        @brief Creates button in the calculator interface for the modulo operation
        @param self: Instance of the class
        """

        button_width, button_height = adjust_button_size(75, 45)
        moduloButton = CTkButton(self.buttonFrame, text="mod", border_width=0, fg_color=COLOR_REST,
                                 corner_radius=10, font=(LARGE, 25),
                                 width=button_width, height=button_height, hover_color=HOVER_COLOR)
        moduloButton.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
        self.buttonFrame.grid_rowconfigure(4, weight=1)
        self.buttonFrame.grid_columnconfigure(0, weight=1)

    def create_settings_button(self):
        """
        @brief Creates a settings/help button in the calculator interface
        @param self: Instance of the class
        """
        settings_image = Image.open(os.path.join("Pictures", "Vrstva 1.png"))
        settings_image = settings_image.resize((50, 50), Image.Resampling.LANCZOS)

        # Create a CTkImage from the resized image
        ctk_settings_image = CTkImage(settings_image)

        settingsButton = CTkButton(self, image=ctk_settings_image, text="", border_width=0, fg_color=DARK_GRAY,
                                   corner_radius=25, font=(LARGE, 15), width=5, height=5,
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
        self.bind(".", lambda event: self.decimal())
        self.bind("=", lambda event: self.equals())

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

# END OF calculator.py file
