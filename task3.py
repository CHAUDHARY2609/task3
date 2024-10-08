import random
def get_computer_choice():
"""Randomly select rock, paper, or scissors for the computer."""
choices = ['rock', 'paper', 'scissors']
return random.choice(choices)
def determine_winner(user_choice, computer_choice):
if user_choice == computer_choice:
return 'tie'
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
(user_choice == 'scissors' and computer_choice == 'paper') or \
(user_choice == 'paper' and computer_choice == 'rock'):
return 'user'
else:
return 'computer'
def play_round():
print("\nRock, Paper, Scissors Game")
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
if user_choice not in ['rock', 'paper', 'scissors']:
print("Invalid choice. Please choose rock, paper, or scissors.")
return None, None
computer_choice = get_computer_choice()
print(f"Computer chose: {computer_choice}")
result = determine_winner(user_choice, computer_choice)
if result == 'tie':
print("It's a tie!")
elif result == 'user':
print("You win!")
else:
print("You lose!")
return result
def main():
user_score = 0
computer_score = 0
while True:
result = play_round()
if result is None:
continue
if result == 'user':
user_score += 1
elif result == 'computer':
computer_score += 1
print(f"\nScore - You: {user_score}, Computer: {computer_score}")
play_again = input("Do you want to play again? (yes/no): ").strip().lower()
if play_again != 'yes':
print("Thank you for playing! Goodbye!")
break
if __name__ == "__main__":
    main()
