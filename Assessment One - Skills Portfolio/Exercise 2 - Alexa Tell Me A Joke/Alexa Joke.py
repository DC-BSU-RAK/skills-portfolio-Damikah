import tkinter as tk
import random

# List of jokes parsed from the provided context (randomJokes.txt)
jokes = [
    {"setup": "Why did the chicken cross the road?", "punchline": "To get to the other side."},
    {"setup": "What happens if you boil a clown?", "punchline": "You get a laughing stock."},
    {"setup": "Why did the car get a flat tire?", "punchline": "Because there was a fork in the road!"},
    {"setup": "How did the hipster burn his mouth?", "punchline": "He ate his pizza before it was cool."},
    {"setup": "What did the janitor say when he jumped out of the closet?", "punchline": "SUPPLIES!!!!"},
    {"setup": "Have you heard about the band 1023MB?", "punchline": "It's probably because they haven't got a gig yet…"},
    {"setup": "Why does the golfer wear two pants?", "punchline": "Because he's afraid he might get a \"Hole-in-one.\""},
    {"setup": "Why should you wear glasses to maths class?", "punchline": "Because it helps with division."},
    {"setup": "Why does it take pirates so long to learn the alphabet?", "punchline": "Because they could spend years at C."},
    {"setup": "Why did the woman go on the date with the mushroom?", "punchline": "Because he was a fun-ghi."},
    {"setup": "Why do bananas never get lonely?", "punchline": "Because they hang out in bunches."},
    {"setup": "What did the buffalo say when his kid went to college?", "punchline": "Bison."},
    {"setup": "Why shouldn't you tell secrets in a cornfield?", "punchline": "Too many ears."},
    {"setup": "What do you call someone who doesn't like carbs?", "punchline": "Lack-Toast Intolerant."},
    {"setup": "Why did the can crusher quit his job?", "punchline": "Because it was soda pressing."},
    {"setup": "Why did the birthday boy wrap himself in paper?", "punchline": "He wanted to live in the present."},
    {"setup": "What does a house wear?", "punchline": "A dress."},
    {"setup": "Why couldn't the toilet paper cross the road?", "punchline": "Because it got stuck in a crack."},
    {"setup": "Why didn't the bike want to go anywhere?", "punchline": "Because it was two-tired!"},
    {"setup": "Want to hear a pizza joke?", "punchline": "Nahhh, it's too cheesy!"},
    {"setup": "Why are chemists great at solving problems?", "punchline": "Because they have all of the solutions!"},
    {"setup": "Why is it impossible to starve in the desert?", "punchline": "Because of all the sand which is there!"},
    {"setup": "What did the cheese say when it looked in the mirror?", "punchline": "Halloumi!"},
    {"setup": "Why did the developer go broke?", "punchline": "Because he used up all his cache."},
    {"setup": "Did you know that ants are the only animals that don't get sick?", "punchline": "It's true! It's because they have little antibodies."},
    {"setup": "Why did the donut go to the dentist?", "punchline": "To get a filling."},
    {"setup": "What do you call a bear with no teeth?", "punchline": "A gummy bear!"},
    {"setup": "What do you call a vegan zombie like to eat?", "punchline": "Graaains."},
    {"setup": "What do you call a dinosaur with only one eye?", "punchline": "A Do-you-think-he-saw-us!"},
    {"setup": "Why should you never fall in love with a tennis player?", "punchline": "Because to them... love means NOTHING!"},
    {"setup": "What did the full glass say to the empty glass?", "punchline": "You look drunk."},
    {"setup": "What's a potato's favorite form of transportation?", "punchline": "The gravy train"},
    {"setup": "What did one ocean say to the other?", "punchline": "Nothing, they just waved."},
    {"setup": "What did the right eye say to the left eye?", "punchline": "Honestly, between you and me something smells."},
    {"setup": "What do you call a dog that's been run over by a steamroller?", "punchline": "Spot!"},
    {"setup": "What's the difference between a hippo and a zippo?", "punchline": "One's pretty heavy and the other's a little lighter"},
    {"setup": "Why don't scientists trust Atoms?", "punchline": "They make up everything."}
]

class JokeAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Joke-Telling Assistant")
        self.root.geometry("500x300")
        
        self.current_joke = None
        
        # Setup labels
        self.setup_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=450)
        self.setup_label.pack(pady=20)
        
        self.punchline_label = tk.Label(self.root, text="", font=("Arial", 12, "italic"), fg="blue", wraplength=450)
        self.punchline_label.pack(pady=10)
        
        # Buttons
        self.tell_joke_button = tk.Button(self.root, text="Alexa tell me a Joke", command=self.tell_joke)
        self.tell_joke_button.pack(pady=5)
        
        self.show_punchline_button = tk.Button(self.root, text="Show Punchline", command=self.show_punchline, state=tk.DISABLED)
        self.show_punchline_button.pack(pady=5)
        
        self.next_joke_button = tk.Button(self.root, text="Next Joke", command=self.next_joke, state=tk.DISABLED)
        self.next_joke_button.pack(pady=5)
        
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=5)
    
    def tell_joke(self):
        self.current_joke = random.choice(jokes)
        self.setup_label.config(text=self.current_joke["setup"])
        self.punchline_label.config(text="")
        self.show_punchline_button.config(state=tk.NORMAL)
        self.next_joke_button.config(state=tk.DISABLED)
    
    def show_punchline(self):
        if self.current_joke:
            self.punchline_label.config(text=self.current_joke["punchline"])
            self.show_punchline_button.config(state=tk.DISABLED)
            self.next_joke_button.config(state=tk.NORMAL)
    
    def next_joke(self):
        self.tell_joke()

if __name__ == "__main__":
    root = tk.Tk()
    app = JokeAssistant(root)
    root.mainloop()
