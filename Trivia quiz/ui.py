from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg = THEME_COLOR, padx = 50, pady = 50)
        self.canvas = Canvas(height = 350, width = 400, bg = "white")
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 40)
        self.question_text = self.canvas.create_text(200, 175, width = 380, text = "Some Question", font = QUESTION_FONT)
        self.right = PhotoImage(file = "./true.png")
        self.wrong = PhotoImage(file = "./false.png")

        self.true_button = Button(image = self.right, highlightthickness = 0, command = self.true_pressed)
        self.true_button.grid(row = 2, column = 0)

        self.false_button = Button(image = self.wrong, highlightthickness = 0, command = self.false_pressed)
        self.false_button.grid(row = 2, column = 1)

        self.score_label = Label(text = "Score: 0", bg = THEME_COLOR, highlightthickness = 0, font = ("Arial", 14))
        self.score_label.grid(row = 0, column = 1)
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg = "white")
        self.score_label.config(text = f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You have reached the end of the quiz.")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)

