from tkinter import *

THEME_COLOR = "#375362"
BACKGROUND = "#ffffff"
CARD_FONT = "Rubik", 20, "italic"


class QuizInterface:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self_score_label = Label(
            text="Score: 0", background=THEME_COLOR, foreground=BACKGROUND)
        self_score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background=BACKGROUND)

        self.question_text = self.canvas.create_text(
            150, 125, text="Some Question Text", fill=THEME_COLOR, font=CARD_FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image, highlightthickness=0, command={})
        self.false_button.grid(row=2, column=0)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command={})
        self.true_button.grid(row=2, column=1)

        self.window.mainloop()
