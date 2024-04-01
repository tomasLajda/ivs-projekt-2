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
