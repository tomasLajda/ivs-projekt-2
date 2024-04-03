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
    @brief Initialization of the top-level window

    @param self: Instance of the class
    @param root: The parent widget
    @param *args: Variable length argument list
    @param **kwargs: Arbitrary keyword arguments
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

        # TODO: FINISH, FIX THE WEIRD BORDER EFFECT
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

        self.helpLabel = CTkLabel(frame, text="Usage", anchor="w", padx=5, pady=10,
                                  font=("Bahnschrift bold", 25), text_color=ORANGE)
        self.helpLabel.grid(row=0, column=0, sticky="nsew")

        subFrame = CTkFrame(frame)
        subFrame.configure(fg_color=GRAY, border_color="black", border_width=1, corner_radius=20)
        subFrame.grid(row=1, column=0, sticky="nsew", pady=10, padx=5)
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
            label_image = CTkLabel(frame_use, image=image, text="")
            label_image.grid(row=row, column=0, sticky="w", padx=10, pady=10)

            label_text = CTkLabel(frame_use, text=text, font=("Bahnschrift bold", 15), text_color="white")
            label_text.grid(row=row, column=1, sticky="w", pady=10, padx=(0, 10))

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

            frame_use.bind("<Configure>", resize_wraplength)
            frame_use.grid_rowconfigure(row, weight=1)

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
                            text="Factorial: Number\n(Num-1)\u00D7(Num-2) \u00D7 ... \u00D7 1\n4! = 4 \u00D7 3 \u00D7 "
                                 "2 \u00D7 1")

        add_image_and_label(subFrame, row=5, image_path=r'Pictures/Abs.ico',
                            text="Absolute value: |Number|\nReturns the distance from 0\n|5| = 5 and |-5| = 5")

        add_image_and_label(subFrame, row=6, image_path=r'Pictures/Mod.ico',
                            text="Modulo: Num % Num = R\nEvaluates the remainder after division\n7 % 3 = 1")

        # =====================================Second part===============================================

        self.helpLabel2 = CTkLabel(frame, text="Specific usage", anchor="w", padx=5, pady=10,
                                   font=("Bahnschrift bold", 25), text_color=ORANGE)
        self.helpLabel2.grid(row=7, column=0, sticky="nsew")

        self.helpLabel3 = CTkLabel(frame, text="More detailed usage of specific buttons\n", anchor="w", padx=5, pady=5,
                                   font=("Bahnschrift bold", 15), text_color="white")
        self.helpLabel3.grid(row=8, column=0, sticky="nsew")

        subFrame2 = CTkFrame(frame)
        subFrame2.configure(fg_color=GRAY, border_color="black", border_width=1, corner_radius=20)
        subFrame2.grid(row=9, column=0, sticky="nsew", pady=5, padx=5)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        add_image_and_label(subFrame2, row=9, image_path=r'Pictures/^.ico',
                            text="How to use Exponentiation: \n1. Choose the base \n2. Select the exponentiaiton "
                                 "button or '^'\n 3. Choose the Exponent")

        add_image_and_label(subFrame2, row=10, image_path=r'Pictures/Root.ico',
                            text="How to use Root: \n1. Choose the degree \n2. Select the root "
                                 "button or 'r'\n 3. Choose the radical")

        add_image_and_label(subFrame2, row=11, image_path=r'Pictures/Fact.ico',
                            text="How to use Factorial: \n1. Choose the number \n2. Select the factorial button or '!'")

        add_image_and_label(subFrame2, row=12, image_path=r'Pictures/Abs.ico',
                            text="How to use Absolute value: \n1. Choose the number \n"
                                 "2. Select the Abs. value button or 'a'")

        add_image_and_label(subFrame2, row=13, image_path=r'Pictures/Mod.ico',
                            text="How to use Modulo: \n1. Choose the number \n"
                                 "2. Select the Modulo buttton or '%'\n"
                                 "3. Choose the divisor")

        # Fixes a bug in the custom tkinter library - places the icon again after 200ms
        self.wm_iconbitmap()
        self.after(200, lambda: self.iconphoto(False, self.help_path))
