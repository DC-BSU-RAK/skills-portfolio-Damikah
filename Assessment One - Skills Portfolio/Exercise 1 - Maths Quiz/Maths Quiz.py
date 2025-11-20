import tkinter as tk
import random
import time

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Quiz")
        self.root.geometry("400x300")
        
        self.score = 0
        self.question_number = 0
        self.difficulty = None
        self.num1 = None
        self.num2 = None
        self.op = None
        self.correct_answer = None
        self.attempt = 1
        
        self.menu_frame = tk.Frame(self.root)
        self.quiz_frame = tk.Frame(self.root)
        self.results_frame = tk.Frame(self.root)
        
        self.displayMenu()
    
    def displayMenu(self):
        self.menu_frame.pack()
        
        tk.Label(self.menu_frame, text="DIFFICULTY LEVEL", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.menu_frame, text="1. Easy", command=lambda: self.selectDifficulty("easy")).pack(pady=5)
        tk.Button(self.menu_frame, text="2. Moderate", command=lambda: self.selectDifficulty("moderate")).pack(pady=5)
        tk.Button(self.menu_frame, text="3. Advanced", command=lambda: self.selectDifficulty("advanced")).pack(pady=5)
    
    def selectDifficulty(self, level):
        self.difficulty = level
        self.menu_frame.pack_forget()
        self.startQuiz()
    
    def startQuiz(self):
        self.score = 0
        self.question_number = 0
        self.nextQuestion()
    
    def nextQuestion(self):
        self.question_number += 1
        if self.question_number > 10:
            self.displayResults()
            return
        
        self.attempt = 1
        self.generateProblem()
        self.displayProblem()
    
    def generateProblem(self):
        self.num1 = self.randomInt(self.difficulty)
        self.num2 = self.randomInt(self.difficulty)
        self.op = self.decideOperation()
        
        if self.op == '-':
            if self.num1 < self.num2:
                self.num1, self.num2 = self.num2, self.num1
        
        if self.op == '+':
            self.correct_answer = self.num1 + self.num2
        else:
            self.correct_answer = self.num1 - self.num2
    
    def randomInt(self, difficulty):
        if difficulty == "easy":
            return random.randint(0, 9)
        elif difficulty == "moderate":
            return random.randint(10, 99)
        elif difficulty == "advanced":
            return random.randint(1000, 9999)
    
    def decideOperation(self):
        return random.choice(['+', '-'])
    
    def displayProblem(self):
        self.quiz_frame.pack()
        
        self.problem_label = tk.Label(self.quiz_frame, text=f"{self.num1} {self.op} {self.num2} =", font=("Arial", 14))
        self.problem_label.pack(pady=10)
        
        self.answer_entry = tk.Entry(self.quiz_frame, font=("Arial", 14))
        self.answer_entry.pack(pady=5)
        
        self.submit_button = tk.Button(self.quiz_frame, text="Submit", command=self.checkAnswer)
        self.submit_button.pack(pady=10)
        
        self.message_label = tk.Label(self.quiz_frame, text="", font=("Arial", 12))
        self.message_label.pack(pady=5)
    
    def checkAnswer(self):
        try:
            user_answer = int(self.answer_entry.get())
        except ValueError:
            self.message_label.config(text="Please enter a valid number.")
            return
        
        if user_answer == self.correct_answer:
            if self.attempt == 1:
                self.score += 10
                self.message_label.config(text="Correct!")
            else:
                self.score += 5
                self.message_label.config(text="Correct on second try!")
            self.root.after(1000, self.clearAndNext)
        else:
            if self.attempt == 1:
                self.attempt = 2
                self.message_label.config(text="Incorrect, try again.")
                self.answer_entry.delete(0, tk.END)
            else:
                self.message_label.config(text="Incorrect, moving on.")
                self.root.after(1000, self.clearAndNext)
    
    def clearAndNext(self):
        self.quiz_frame.pack_forget()
        self.nextQuestion()
    
    def displayResults(self):
        self.results_frame.pack()
        
        rank = self.getRank()
        tk.Label(self.results_frame, text=f"Your score: {self.score}/100", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.results_frame, text=f"Rank: {rank}", font=("Arial", 14)).pack(pady=5)
        
        tk.Button(self.results_frame, text="Play Again", command=self.playAgain).pack(pady=10)
        tk.Button(self.results_frame, text="Quit", command=self.root.quit).pack(pady=5)
    
    def getRank(self):
        if self.score >= 90:
            return "A+"
        elif self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        elif self.score >= 50:
            return "D"
        else:
            return "F"
    
    def playAgain(self):
        self.results_frame.pack_forget()
        self.displayMenu()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


