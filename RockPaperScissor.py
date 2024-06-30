import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.configure(bg="#add8e6") 

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()
    
    def create_widgets(self):
        self.header_label = tk.Label(self.root, text="Rock-Paper-Scissors Game", font=("Arial", 20, "bold"), bg="#add8e6")
        self.header_label.grid(row=0, column=0, columnspan=4, pady=20)
        
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14), bg="#add8e6")
        self.label.grid(row=1, column=0, columnspan=4, pady=10)

        self.button_frame = tk.Frame(self.root, bg="#add8e6")
        self.button_frame.grid(row=2, column=0, columnspan=4, pady=10)
        
        self.rock_button = tk.Button(self.button_frame, text="Rock", width=10, font=("Arial", 12), bg="#d3d3d3", command=lambda: self.play_round("rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", width=10, font=("Arial", 12), bg="#d3d3d3", command=lambda: self.play_round("paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=10, font=("Arial", 12), bg="#d3d3d3", command=lambda: self.play_round("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 18), bg="#add8e6")
        self.result_label.grid(row=3, column=0, columnspan=4, pady=10)
        
        self.score_label = tk.Label(self.root, text=f"Scores - You: {self.user_score}, Computer: {self.computer_score}", font=("Arial", 15), bg="#add8e6")
        self.score_label.grid(row=5, column=0, columnspan=4, pady=10)
        
        self.play_again_button = tk.Button(self.root, text="Play Again", width=10, font=("Arial", 12), bg="#d3d3d3", command=self.reset_game)
        self.play_again_button.grid(row=6, column=0, columnspan=4, pady=10)
    
    def play_round(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        winner = self.determine_winner(user_choice, computer_choice)
        
        self.result_label.config(text=f"You chose: {user_choice},\nComputer chose: {computer_choice}\n\n{winner}")
        
        if winner == "You win!":
            self.user_score += 1
        elif winner == "You lose!":
            self.computer_score += 1
        
        self.score_label.config(text=f"Scores - You: {self.user_score}, Computer: {self.computer_score}")
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "You win!"
        else:
            return "You lose!"
    
    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text=f"Scores - You: {self.user_score}, Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
