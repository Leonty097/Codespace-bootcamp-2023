import random #Import random library to use it
#Initialize the counter variables on 0
tie = 0
wins = 0
losses = 0

#Create a function to be called each time you need the cpu randomly choose a move
def cpu_random():
    return random.randint(1, 3)
#Asociate numbers between 1 to 3 to our predefined strings
def get_cpu_move(random_int):
    if random_int == 1:
        return "rock"
    elif random_int == 2:
        return "paper"
    else:
        return "scissors"
# Create another function for solution it will evaluate wins and ties, losses will fall into the else statement
def solution(user_move, cpu_move):
    #use the global keyword to be asoaciate with our counter out of the scope of this fuction
    #Therefore it will be updated each loop
    global tie, wins, losses

    if user_move == "rock" and cpu_move == "scissors":
        print("User wins!")
        wins += 1
    elif user_move == "paper" and cpu_move == "rock":
        print("User wins!")
        wins += 1
    elif user_move == "scissors" and cpu_move == "paper":
        print("User wins!")
        wins += 1
    elif user_move == cpu_move:
        print("It's a tie!")
        tie += 1
    else:
        print("User loses :c")
        losses += 1
#first line to introduce the game
print("Hello! welcome to a simple Rock, Paper, Scissors game \nTo start playing, select your move")

#While cicle to be reapeated each time that the user select "y" to continue playing
while True:
#Get the user input and link into our predefined strings
    user_input = input("Select! (r = rock, p = paper, s = scissors): ")
    if user_input == "r":
        user_move = "rock"
    elif user_input == "p":
        user_move = "paper"
    elif user_input == "s":
        user_move = "scissors"
    else:
        print("Invalid input. Please select 'r', 'p', or 's'.")
        continue

# Print the user's selected move
print(f"You selected {user_move}")

# Get a random move for the CPU using the cpu_random function
cpu_random_result = cpu_random()
# Map the random integer result to an actual move using get_cpu_move function
cpu_move_result = get_cpu_move(cpu_random_result)
# Print the CPU's selected move
print(f"CPU selected {cpu_move_result}")

# Call the solution function to determine the game outcome
solution(user_move, cpu_move_result)

# Print the current statistics of the game (Wins, Ties, Losses)
print(f"Wins: {wins}, Ties: {tie}, Losses: {losses}")

#Implement a repl
    re_play = input("Would you like to play again? (y/n): ")
    if re_play.lower() == "n":
        print("Thanks for playing. Come back when you want to!")
        break
    elif re_play.lower() == "y":
        continue
    else:
        print("Invalid input. Thanks for playing!")
        break
