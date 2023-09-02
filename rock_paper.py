import tkinter as tk
import random

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Set the window size (width x height)
window.geometry("400x200")  # Adjust the size as needed

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Label and dropdown for user choice
user_choice_label = tk.Label(window, text="Choose Rock, Paper, or Scissors:")
user_choice_label.pack()

user_choice_var = tk.StringVar()
user_choice_dropdown = tk.OptionMenu(window, user_choice_var, *choices)
user_choice_dropdown.pack()

# Button to play the game
play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()

# Label to display the result
result_label = tk.Label(window, text="", font=("Helvetica", 16, "bold"))
result_label.pack()

# Run the Tkinter main loop
window.mainloop()
