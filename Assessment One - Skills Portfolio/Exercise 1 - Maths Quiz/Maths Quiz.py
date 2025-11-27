import tkinter as tk
import random
from tkinter import messagebox



class ArithmeticQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Quiz")

        # Set global background color
        self.root.configure(bg="black")

        self.score = 0
        self.question_count = 0
        self.difficulty = 0
        self.current_answer = 0
        self.attempts = 0
        self.questions_per_quiz = 10

        # Set up frames with black backgrounds
        self.menu_frame = tk.Frame(self.root, bg="black")
        self.quiz_frame = tk.Frame(self.root, bg="black")
        self.results_frame = tk.Frame(self.root, bg="black")

        # Initialize UI elements
        self.displayMenu()
        self.setup_quiz_frame()
        self.setup_results_frame()

        # Show the initial menu frame
        self.menu_frame.pack(fill='both', expand=True)

    # --- Core Functions ---

    def displayMenu(self):
        """A function that displays the difficulty level menu at the beginning of the quiz."""
        tk.Label(self.menu_frame, text="DIFFICULTY LEVEL", font=("Helvetica", 16),
                 bg="black", fg="white").pack(pady=20)

        tk.Button(self.menu_frame, text="1. Easy (Single Digit)", bg="#35A66A",
                  command=lambda: self.start_quiz(1)).pack(pady=5)

        tk.Button(self.menu_frame, text="2. Moderate (Double Digit)", bg="#CBC947",
                  command=lambda: self.start_quiz(2)).pack(pady=5)

        tk.Button(self.menu_frame, text="3. Advanced (4-Digit)", bg="#A63535",
                  command=lambda: self.start_quiz(4)).pack(pady=5)

    def setup_quiz_frame(self):
        """Sets up the widgets for the quiz screen."""
        self.question_label = tk.Label(self.quiz_frame, text="", font=("Helvetica", 20),
                                       bg="black", fg="white")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.quiz_frame, font=("Helvetica", 16), insertbackground="white")
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.quiz_frame, text="Submit Answer",
                                       command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(self.quiz_frame, text="", fg="blue", bg="black")
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(self.quiz_frame, text="Score: 0/0",
                                    bg="black", fg="white")
        self.score_label.pack(pady=10)

    def setup_results_frame(self):
        """Sets up the widgets for the results screen."""
        self.results_title = tk.Label(self.results_frame, text="Quiz Results",
                                      font=("Helvetica", 18), bg="black", fg="white")
        self.results_title.pack(pady=20)
        
        self.final_score_label = tk.Label(self.results_frame, text="",
                                          font=("Helvetica", 16), bg="black", fg="white")
        self.final_score_label.pack(pady=10)

        self.rank_label = tk.Label(self.results_frame, text="",
                                   font=("Helvetica", 16), bg="black", fg="white")
        self.rank_label.pack(pady=10)

        self.replay_button = tk.Button(self.results_frame, text="Play Again?",
                                       command=self.reset_quiz)
        self.replay_button.pack(pady=20)


    def start_quiz(self, difficulty_level):
        """Starts the quiz with the chosen difficulty."""
        self.difficulty = difficulty_level
        self.score = 0
        self.question_count = 0
        self.menu_frame.pack_forget()
        self.quiz_frame.pack(fill='both', expand=True)
        self.displayProblem()

    def randomInt(self, difficulty):
        """Returns a random integer based on difficulty level (e.g., single, double, 4-digit)."""
        if difficulty == 1:
            return random.randint(1, 9)
        elif difficulty == 2:
            return random.randint(10, 99)
        else:  # 4 digits
            return random.randint(1000, 9999)

    def decideOperation(self):
        """Randomly decides whether the problem is addition or subtraction."""
        return random.choice(['+', '-'])

    def displayProblem(self):
        """Displays the question and resets entry box."""
        num1 = self.randomInt(self.difficulty)
        num2 = self.randomInt(self.difficulty)
        operation = self.decideOperation()

        if operation == '-' and num2 > num1:
            num1, num2 = num2, num1

        problem_text = f"{num1} {operation} {num2} ="

        if operation == '+':
            self.current_answer = num1 + num2
        else:
            self.current_answer = num1 - num2
        
        self.question_label.config(text=problem_text)
        self.feedback_label.config(text="")
        self.answer_entry.delete(0, tk.END)
        self.attempts = 1
        self.question_count += 1
        self.update_score_label()

    def update_score_label(self):
        """Updates the score label in the quiz frame."""
        self.score_label.config(
            text=f"Score: {self.score}/{self.question_count - 1} | Question {self.question_count}/{self.questions_per_quiz}"
        )

    def check_answer(self):
        """Manages answer checking and scoring logic."""
        try:
            user_answer = int(self.answer_entry.get())
            if self.isCorrect(user_answer):
                points = 10 if self.attempts == 1 else 5
                self.score += points
                self.feedback_label.config(
                    text=f"Correct! You earned {points} points.", fg="green"
                )
                
                if self.question_count == self.questions_per_quiz:
                    self.end_quiz()
                else:
                    self.root.after(1500, self.displayProblem)
            else:
                if self.attempts == 1:
                    self.attempts += 1
                    self.feedback_label.config(
                        text="Wrong answer. Try again (one chance left).", fg="red"
                    )
                else:
                    self.feedback_label.config(
                        text=f"Wrong again. The answer was {self.current_answer}.", fg="orange"
                    )
                    if self.question_count == self.questions_per_quiz:
                        self.root.after(1500, self.end_quiz)
                    else:
                        self.root.after(1500, self.displayProblem)
        except ValueError:
            self.feedback_label.config(text="Please enter a valid integer.", fg="red")

    def isCorrect(self, user_answer):
        """Checks if the answer is correct."""
        return user_answer == self.current_answer

    def displayResults(self):
        """Displays the final score and rank."""
        self.quiz_frame.pack_forget()
        self.results_frame.pack(fill='both', expand=True)

        percentage = (self.score / (self.questions_per_quiz * 10)) * 100
        
        if percentage >= 90:
            rank = "A+ (Excellent!)"
        elif percentage >= 80:
            rank = "A (Great job!)"
        elif percentage >= 70:
            rank = "B (Good effort)"
        elif percentage >= 60:
            rank = "C (Keep practicing)"
        else:
            rank = "D (Need improvement)"

        self.final_score_label.config(
            text=f"Your Final Score: {self.score}/100 ({percentage:.1f}%)"
        )
        self.rank_label.config(text=f"Rank: {rank}")
    
    def end_quiz(self):
        """Moves to results screen."""
        self.score_label.config(text=f"Score: {self.score}/100 | Quiz Complete") 
        self.root.after(1500, self.displayResults)

    def reset_quiz(self):
        """Resets and returns to the menu."""
        self.results_frame.pack_forget()
        self.score = 0
        self.question_count = 0
        self.displayMenu()

    

if __name__ == "__main__":
    root = tk.Tk()
    quiz = ArithmeticQuiz(root)  
    root.mainloop()
