"""
@file help_menu.py
@brief File containing the help menu

@author
- Martin Valapka (xvalapm00)

@date - April 3, 2024
"""

from PIL import Image, ImageTk
from customtkinter import *
import platform

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
    @brief Top-level window for displaying help information

    @param root: The parent widget

    Attributes:
        help_path (str): The path to the help image
    """

    def __init__(self, root, *args, **kwargs):
        """
        @brief Initializes the top-level window.

        This method initializes the top-level window and configures its appearance based on the platform

        @param self: Instance of the class
        @param root: The parent widget
        @param *args: Variable length argument list
        @param **kwargs: Arbitrary keyword arguments
        """

        # TODO: ADD MORE DESCRIPTION
        super().__init__(*args, **kwargs)

        if platform.system() == 'Linux':
            self.geometry(f"400x350+{root.winfo_x() + 40}+{root.winfo_y() + 65}")
        else:
            self.geometry(f"300x300+{root.winfo_x() + 65}+{root.winfo_y() + 80}")

        self.resizable(True, True)
        self.title("Help")
        self.help_path = ImageTk.PhotoImage(file=os.path.join("Pictures", 'questionmark1_83827.png'))
        self.wm_iconbitmap()
        self.iconphoto(False, self.help_path)

        frame = CTkScrollableFrame(self)
        frame.configure(fg_color=DARK_GRAY)
        frame.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.helpLabel = CTkLabel(frame, text="About", anchor="center", padx=5, pady=10,
                                  font=("Arial", 25, "bold"), text_color=ORANGE)
        self.helpLabel.grid(row=0, column=0, sticky="nsew")

        aboutFrame = CTkFrame(frame)
        aboutFrame.configure(fg_color=GRAY, border_color="black", border_width=1, corner_radius=20)
        aboutFrame.grid(row=1, column=0, sticky="nsew", pady=10, padx=5)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        self.helpLabel = CTkLabel(frame, text="Usage", anchor="w", padx=5, pady=10,
                                  font=("Arial", 25, "bold"), text_color=ORANGE)
        self.helpLabel.grid(row=2, column=0, sticky="nsew")

        subFrame = CTkFrame(frame)
        subFrame.configure(fg_color=GRAY, border_color="black", border_width=1, corner_radius=20)
        subFrame.grid(row=3, column=0, sticky="nsew", pady=10, padx=5)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        def add_image_and_label(frame_use, row, image_path, text):
            """
            @brief Adds an image and label to a given frame.

            This method adds an image and a corresponding label to a specified frame

            @param frame_use: The frame to which the image and label will be added
            @param row: The row in which the image and label will be placed
            @param image_path: The path to the image file
            @param text: The text for the label
            """

            image = CTkImage(Image.open(image_path), size=(45, 35))
            labelImage = CTkLabel(frame_use, image=image, text="")
            labelImage.grid(row=row, column=0, sticky="w", padx=10, pady=15)

            labelText = CTkLabel(frame_use, text=text, font=("Arial", 15), text_color="white")
            labelText.grid(row=row, column=1, sticky="w", pady=15, padx=(0, 10))

            def resize_wraplength(event):
                """
                @brief Resizes the wrap length of the label text based on the event width

                This function adjusts the wrap length of the label text based on the width of the event

                @param event: Event(resizing) triggering the resizing
                """

                if platform.system() == 'Linux':
                    labelText.configure(wraplength=event.width - 70)
                else:
                    labelText.configure(wraplength=event.width - 140)

            frame_use.bind("<Configure>", resize_wraplength)
            frame_use.grid_rowconfigure(row, weight=1)

        # =====================================About part===============================================
        aboutText = """Simple calculator developed by: 
        xcsirim00, xgajduv00, xlajdat00 a xvalapm00\n 
        It supports basic arithmetic operations: 
        Addition, subtraction, multiplication, and division. 
        Additionally, it provides features like: 
        Exponentiation, root, factorial, absolute value and modulo. 
        It also supports decimal numbers and negative numbers.\n 
        Enjoy calculating!\n 
        The Calculator is divided into 2 frames - display and buttons. 
        The display frame shows the current expression and the result. 
        While the button frame contains buttons for inputting numbers, operators, and performing various operations.\n 
        The evaluation works automatically when you press the operator or when you press the equals button. 
        You can also perform calculations by typing directly on the keyboard, and the calculator will update accordingly.\n 
        The calculator takes maximum two operands at the same time (brackets not implemented) and performs the specified operation between them. 
        When you make a mistake with choosing the operator, you can directly change it by selecting your desired operator.\n 
        The current expression is limited to 14 characters, while the total expression can accommodate up to 30 characters."""

        label_text = CTkLabel(aboutFrame, text=aboutText, font=("Arial", 15), text_color="white")
        label_text.grid(row=0, column=0, sticky="nsew", pady=10, padx=0)
        aboutFrame.grid_rowconfigure(0, weight=1)

        def resize_wraplength(event):
            """
            @brief Resizes the wrap length of the label text based on the event width

            This function adjusts the wrap length of the label text based on the width of the event

            @param event: Event(resizing) triggering the resizing
            """

            if platform.system() == 'Linux':
                label_text.configure(wraplength=event.width - 70)
            else:
                label_text.configure(wraplength=event.width - 140)

        aboutFrame.bind("<Configure>", resize_wraplength)

        # =====================================First part===============================================

        add_image_and_label(subFrame, row=0, image_path=r'Pictures/Clear.ico',
                            text="Clears both the current and total expression")

        add_image_and_label(subFrame, row=1, image_path=r'Pictures/Del.ico',
                            text="Erases the last digit/operator in the current expression")

        add_image_and_label(subFrame, row=2, image_path=r'Pictures/^.ico',
                            text="Exponentiation: \nBase^Exponent = Product\n5^2 = 25")

        add_image_and_label(subFrame, row=3, image_path=r'Pictures/Root.ico',
                            text="Root: ⁿ√x = Root\nn - degree, x - radical\n²√25 = 5")

        add_image_and_label(subFrame, row=4, image_path=r'Pictures/Fact.ico',
                            text="Factorial: Number!\n(Num-1)\u00D7(Num-2) \u00D7 ... \u00D7 1\n4! = 4 \u00D7 3 \u00D7 "
                                 "2 \u00D7 1")

        add_image_and_label(subFrame, row=5, image_path=r'Pictures/Abs.ico',
                            text="Absolute value: |Number|\nReturns the distance from 0\n|5| = 5 and |-5| = 5")

        add_image_and_label(subFrame, row=6, image_path=r'Pictures/Mod.ico',
                            text="Modulo: Num % Num = R\nEvaluates the remainder after division\n7 % 3 = 1")

        add_image_and_label(subFrame, row=7, image_path=r'Pictures/add.ico',
                            text="Addition: Num + Num = Sum\nReturns the sum after addition\n7 + 3 = 10")

        add_image_and_label(subFrame, row=8, image_path=r'Pictures/sub.ico',
                            text="Subtraction: Num - Num = Difference\nReturns the difference after subtraction"
                                 "\n7 - 3 = 4")

        add_image_and_label(subFrame, row=9, image_path=r'Pictures/mul.ico',
                            text="Multiplication: Num \u00D7 Num = Product\nReturns the product after multiplication"
                                 "\n7 \u00D7 3 = 21")

        add_image_and_label(subFrame, row=10, image_path=r'Pictures/div.ico',
                            text="Division: Num \u00F7 Num = Quotient\nReturns the quotient after division\n"
                                 "Num \u00F7 0 = Division error"
                                 "\n10 \u00F7 2 = 5")

        add_image_and_label(subFrame, row=11, image_path=r'Pictures/equals.ico',
                            text="Equals: Evaluates the expression:\nFrom the total and current expression\n"
                                 "Clears the total expression\n"
                                 "Prints the result to the current expression")

        add_image_and_label(subFrame, row=12, image_path=r'Pictures/brackets.ico',
                            text="Brackets: NOT IMPLEMENTED\nUseless in this version of calculator"
                                 "\nMight be implemented later")

        add_image_and_label(subFrame, row=13, image_path=r'Pictures/decimal.ico',
                            text="Decimal point: Places decimal point in the current expression"
                                 "\nRounds the number if there are only zeroes behind the decimal point\n"
                                 "Removes trailing decimal point if no digit follows it")
        # =====================================Second part===============================================

        self.helpLabel2 = CTkLabel(frame, text="Specific usage", anchor="w", padx=5, pady=10,
                                   font=("Arial", 25, "bold"), text_color=ORANGE)
        self.helpLabel2.grid(row=14, column=0, sticky="nsew")

        self.helpLabel3 = CTkLabel(frame, text="More detailed usage of specific buttons\n", anchor="w", padx=5, pady=5,
                                   font=("Arial", 15, "bold"), text_color="white")
        self.helpLabel3.grid(row=15, column=0, sticky="nsew")

        subFrame2 = CTkFrame(frame)
        subFrame2.configure(fg_color=GRAY, border_color="black", border_width=1, corner_radius=20)
        subFrame2.grid(row=16, column=0, sticky="nsew", pady=5, padx=5)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        add_image_and_label(subFrame2, row=17, image_path=r'Pictures/^.ico',
                            text="How to use Exponentiation: \n1. Choose the base \n2. Select the exponentiation "
                                 "button\n 3. Choose the Exponent \n 4. Exponent cannot be decimal or negative")

        add_image_and_label(subFrame2, row=18, image_path=r'Pictures/Root.ico',
                            text="How to use Root: \n1. Choose the degree \n2. Select the root "
                                 "button\n 3. Choose the radical \n4. Radical follows mathematical rules + cannot be "
                                 "decimal")

        add_image_and_label(subFrame2, row=19, image_path=r'Pictures/Fact.ico',
                            text="How to use Factorial: \n1. Choose the number - not negative or decimal \n2. Select "
                                 "the factorial button or '!'")

        add_image_and_label(subFrame2, row=20, image_path=r'Pictures/Abs.ico',
                            text="How to use Absolute value: \n1. Choose the number \n"
                                 "2. Select the Abs. value button")

        add_image_and_label(subFrame2, row=21, image_path=r'Pictures/Mod.ico',
                            text="How to use Modulo: \n1. Choose the number \n"
                                 "2. Select the Modulo button\n"
                                 "3. Choose the divisor except 0")

        # Fixes a bug in the custom tkinter library - places the icon again after 200ms
        self.wm_iconbitmap()
        self.after(200, lambda: self.iconphoto(False, self.help_path))
