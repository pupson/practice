from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Trivia Game')

        self.window.minsize(width=300, height=250)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.trivia_text = self.canvas.create_text(150, 125, width=280, text='', fill='black', font=(FONT, 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=(FONT, 10, 'bold'))
        self.score_label.grid(column=1, row=0, sticky="EW")

        self.card_true_img = PhotoImage(file='images/true.png')
        self.card_true_button = Button(image=self.card_true_img, highlightthickness=0, command=self.question_true)
        self.card_true_button.grid(column=0, row=2)

        self.card_false_img = PhotoImage(file='images/false.png')
        self.card_false_button = Button(image=self.card_false_img, highlightthickness=0, command=self.question_false)
        self.card_false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.trivia_text, text= q_text)
        else:
            self.canvas.itemconfig(self.trivia_text, text='End of quiz.')
            self.card_false_button.config(state='disabled')
            self.card_true_button.config(state='disabled')

    def question_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def question_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)