from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
ACCENT_COLOR = "#537d93"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Window, Window Config & Canvas
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizix")
        self.window.eval('tk::PlaceWindow . center')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(bg=ACCENT_COLOR, height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Labels
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg='#FFFFFF',
                                 font=('Arial', 12, "bold"))
        self.score_label.grid(row=0, column=1)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text!",
            fill='#FFFFFF',
            font=('Arial', 20, 'italic')
        )

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(self.window, image=true_img, command=self.answer_true,
                               bg=THEME_COLOR, highlightthickness=0)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(self.window, image=false_img, command=self.answer_false,
                                bg=THEME_COLOR, highlightthickness=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        # Game loop
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=ACCENT_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. "
                                                            f"Your final score {self.quiz.score} / 10! Play again?")
            self.true_btn.config(command=quit)
            self.false_btn.config(command=quit)

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
