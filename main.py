import random

def play_rock_paper_scissors():
  """Plays a single round of Rock Paper Scissors."""

  player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

  # Validate user input 
  while player_choice not in ["rock", "paper", "scissors"]:
    player_choice = input("Invalid choice. Please enter 'rock', 'paper', or 'scissors': ").lower()

  # Computer's random choice
  computer_choice = random.choice(["rock", "paper", "scissors"])

  print(f"You chose: {player_choice}")
  print(f"Computer chose: {computer_choice}")

  # Determine the winner
  if player_choice == computer_choice:
    print("It's a tie!")
  elif (
      (player_choice == "rock" and computer_choice == "scissors") or
      (player_choice == "paper" and computer_choice == "rock") or
      (player_choice == "scissors" and computer_choice == "paper")
  ):
    print("You win!")
  else:
    print("Computer wins!")

# Start the game
play_rock_paper_scissors()