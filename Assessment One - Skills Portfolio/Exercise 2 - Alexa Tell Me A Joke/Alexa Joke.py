import tkinter as tk
import random

# Load jokes from file
def load_jokes(filename="randomJokes.txt"):
    jokes = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if "?" in line:
                    setup, punchline = line.split("?", 1)
                    jokes.append((setup + "?", punchline.strip()))
    except FileNotFoundError:
        jokes = [("File not found!", "Please ensure randomJokes.txt is in the folder.")]
    return jokes


# GLOBAL joke list
jokes = load_jokes()


class JokeAssistant:
    def __init__(self, root):
        self.root = root

        # Phone-style window layout
        self.root.title("Joke Assistant")
        self.root.geometry("360x640")          # Phone aspect ratio
        self.root.configure(bg="#111")         # Dark phone bezel
        self.root.resizable(False, False)

        # Phone screen (white panel)
        self.screen = tk.Frame(self.root, bg="white", width=330, height=600)
        self.screen.place(relx=0.5, rely=0.5, anchor="center")

        # Fake phone top bar
        tk.Label(
            self.screen, 
            text="📱 Joke-Telling Assistant", 
            bg="#222", 
            fg="white", 
            font=("Arial", 14, "bold"),
            height=2
        ).pack(fill="x")

        self.current_joke = None 

        # Joke text area
        self.setup_label = tk.Label(
            self.screen, text="", font=("Arial", 14),
            wraplength=300, bg="white", fg="black"
        )
        self.setup_label.pack(pady=20)

        self.punchline_label = tk.Label(
            self.screen, text="", font=("Arial", 12, "italic"),
            wraplength=300, fg="blue", bg="white"
        )
        self.punchline_label.pack(pady=10)

        # Button style
        btn_style = {
            "font": ("Arial", 12, "bold"),
            "width": 22,
            "height": 1,
            "bg": "#007AFF",
            "fg": "white",
            "bd": 0,
            "activebackground": "#005BBB"
        }

        self.tell_joke_button = tk.Button(
            self.screen, text="Alexa, tell me a joke",
            command=self.tell_joke, **btn_style
        )
        self.tell_joke_button.pack(pady=8)

        self.show_punchline_button = tk.Button(
            self.screen, text="Show Punchline", state=tk.DISABLED,
            command=self.show_punchline, **btn_style
        )
        self.show_punchline_button.pack(pady=8)

        self.next_joke_button = tk.Button(
            self.screen, text="Next Joke", state=tk.DISABLED,
            command=self.next_joke, **btn_style
        )
        self.next_joke_button.pack(pady=8)

        self.quit_button = tk.Button(
            self.screen, text="Quit", command=self.root.quit,
            **btn_style
        )
        self.quit_button.pack(pady=8)

    def tell_joke(self):
        self.current_joke = random.choice(jokes)
        setup, punchline = self.current_joke
        self.setup_label.config(text=setup)
        self.punchline_label.config(text="")

        self.show_punchline_button.config(state=tk.NORMAL)
        self.next_joke_button.config(state=tk.DISABLED)

    def show_punchline(self):
        if self.current_joke:
            self.punchline_label.config(text=self.current_joke[1])
            self.show_punchline_button.config(state=tk.DISABLED)
            self.next_joke_button.config(state=tk.NORMAL)

    def next_joke(self):
        self.tell_joke()


if __name__ == "__main__":
    root = tk.Tk()
    app = JokeAssistant(root)
    root.mainloop()
