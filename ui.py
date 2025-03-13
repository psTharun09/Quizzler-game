from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.Label = Label(
            text=f"Score:{self.score}",
            bg=THEME_COLOR,
            highlightthickness=0,
            fg="white",
            font=15)
        self.Label.grid(row=0, column=1)

        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.Question_text =self.canvas.create_text(
            150,125,
            width=280,
            text="Something",
            font=("Arial",20,"italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.cross_img = PhotoImage(file="images/false.png")
        self.crt_img = PhotoImage(file="images/true.png")

        self.cross_button = Button(image=self.cross_img,highlightthickness=0,command=self.false)
        self.cross_button.grid(row=2,column=1)

        self.crt_button = Button(image=self.crt_img, highlightthickness=0,command=self.true)
        self.crt_button.grid(row=2, column=0)

        self.get_next_Question()

        self.window.mainloop()

    def get_next_Question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.Question_text,text=q_text)
        self.crt_button.config(command=self.true)
        self.cross_button.config(command=self.false)

    def true(self):
        if self.quiz.check_answer(user_answer="True"):
            self.score += 1
            self.Label.config(text=f"Score:{self.score}")
            self.canvas.config(bg="green")
            self.crt_button.config(command=self.dummy)
            self.cross_button.config(command=self.dummy)
            if self.still_has_quiz():
                self.window.after(ms=3000,func=self.get_next_Question)
            else:
                self.window.after(ms=3000, func=self.game_over)
        else:
            self.canvas.config(bg="red")
            self.crt_button.config(command=self.dummy)
            self.cross_button.config(command=self.dummy)
            if self.still_has_quiz():
                self.window.after(ms=3000, func=self.get_next_Question)
            else:
                self.window.after(ms=3000,func=self.game_over)

    def false(self):
        if self.quiz.check_answer(user_answer="False"):
            self.score += 1
            self.Label.config(text=f"Score:{self.score}")
            self.canvas.config(bg="green")
            self.crt_button.config(command=self.dummy)
            self.cross_button.config(command=self.dummy)
            if self.still_has_quiz():
                self.window.after(ms=3000, func=self.get_next_Question)
            else:
                self.window.after(ms=3000, func=self.game_over)
        else:
            self.canvas.config(bg="red")
            self.crt_button.config(command=self.dummy)
            self.cross_button.config(command=self.dummy)
            if self.still_has_quiz():
                self.window.after(ms=3000, func=self.get_next_Question)
            else:
                self.window.after(ms=3000, func=self.game_over)

    def still_has_quiz(self):
        return self.quiz.still_has_questions()

    def game_over(self):
        self.window.config(bg="blue")
        self.canvas.config(bg="blue")
        self.canvas.itemconfig(
            self.Question_text,
            text=f"GAME OVER!\n\nYou have scored\n\n{self.score}/{self.quiz.question_number}",
            fill="black",
            font=("Arial",20,"bold"),
        )
        self.Label.grid_forget()
        self.cross_button.grid_forget()
        self.crt_button.grid_forget()

    def dummy(self):
        pass