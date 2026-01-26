import random

print("Rock Paper Scissors - Best of 3")
print("Choose your option by number each round:")
print("1 = Rock | 2 = Paper | 3 = Scissors")

choices = ["rock", "paper", "scissors"]

while True:  # main loop to replay
    user_score = 0
    computer_score = 0
    round_num = 1

    while round_num <= 3:
        print(f"\nRound {round_num}")
        
        # Input validation loop
        while True:
            user_input = input("Enter your choice (1/2/3): ")
            if user_input in ["1", "2", "3"]:
                break  # valid input
            print("Invalid input! Please enter 1, 2, or 3.")

        user = choices[int(user_input)-1]  # convert number to choice
        computer = random.choice(choices)

        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        # decide winner
        if user == computer:
            print("It's a tie this round!")
        elif ((user == "rock" and computer == "scissors") or 
             (user == "paper" and computer == "rock") or 
             (user == "scissors" and computer == "paper")):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        round_num += 1

    # final results
    print("\nFinal Score:")
    print(f"You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Computer won the game! Better luck next time!")
    else:
        print("It's a tie game!")

    # replay prompt with input validation
    while True:
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay in ["yes", "no"]:
            break
        print(" Please type 'yes' or 'no'.")

    if replay == "no":
        print("Thanks for playing! Bye!")
        break
