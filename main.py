
import random
import calculateWinner

# Rock-Paper-Scissors game

# -----------------------------------------------------------------------
"""
Get the players choices.
@param: choices
    Array of choices
@return: player
    the player's choice
"""


def get_player_choice(choices):
    player = ""
    while player not in choices:
        player = input("Enter rock, paper, or scissors: ").lower().capitalize()
        if player not in choices:
            print("Please enter a valid argument.")

    return player


# -----------------------------------------------------------------------
"""
Get the amount of wins needed to win the series.
@return: needed_wins
"""


def get_needed_wins():

    needed_wins = input("How many wins would you like to play to? ")

    while (not needed_wins.isdigit()):
        print("Please enter a valid natural number.")
        print()
        needed_wins = input("How many wins would you like to play to? ")

    while (int(needed_wins) > 10 or int(needed_wins) <= 0):
        print("Hmm... Let's choose a better number. Maybe between 1-10?")
        print()
        needed_wins = get_needed_wins()

    return int(needed_wins)


# -----------------------------------------------------------------------
"""
Print the scoreboard
@param: cWins
  computer's number of wins
@param: pWins
  player's number of wins
@param: needed_wins
  the number of wins playing to
"""


def print_scoreboard(cWins, pWins, needed_wins):
    print()
    print("*** SCOREBOARD ***")
    print("You: ........... " + str(pWins))
    print("Computer: ...... " + str(cWins))
    print("Playing to {} win(s)".format(str(needed_wins)))
    print("******************")
    print()


# -----------------------------------------------------------------------
"""
Play games of Rock-Paper-Scissors until either the computer or the player reach
the needed amount of wins to win the series.
@param: cWins
  number of computer wins
@param: pWins
  number of player wins
@param: needed_wins
  number of wins needed to win the series
@param: choices
  the array of choices to choose from
@return: absWinner, cWins, pWins
  the absolute winner AKA who won the series
"""


def play_games(needed_wins, choices):
    cWins = 0
    pWins = 0
    while ((cWins < needed_wins) and (pWins < needed_wins)):
        player = get_player_choice(choices)
        computer = random.choice(choices)

        winner = ""
        match player:
            case "Rock":
                winner = calculateWinner.rock(computer)
            case "Paper":
                winner = calculateWinner.paper(computer)
            case "Scissors":
                winner = calculateWinner.scissors(computer)

        if (winner == "player"):
            print("I played {}, you won that round!".format(computer))
            pWins += 1
        elif (winner == "computer"):
            print("I played {}, you lost that round!".format(computer))
            cWins += 1
        else:
            print("It was a tie!")

        print_scoreboard(cWins, pWins, needed_wins)
    # End while

    if (pWins > cWins):
        absWinner = "player"
    else:
        absWinner = "computer"

    return absWinner, cWins, pWins


# -----------------------------------------------------------------------
"""
Output who won the series
@param: winner
  who won the series
@param: cWins
  number of computer wins
@param: pWins
  number of player wins
"""


def print_winner(winning_info):
    winner = winning_info[0]
    cWins = winning_info[1]
    pWins = winning_info[2]
    if (winner == "player"):
        print(
            "Drat! You got me this time. You won {0}-{1}.".format(str(pWins), str(cWins)))
    else:
        print(
            "HAHAHA! I've bested you {1}-{0}. You lose!".format(str(pWins), str(cWins)))


# MAIN ------------------------------------------------------------------
# Array of choices
choices = ["Rock", "Paper", "Scissors"]

# Start game
print("Let's play Rock-Paper-Scissors!")
print()
needed_wins = get_needed_wins()
print()

# Ready?!
ready = input("It's time to battle! Are you ready?! (Type 'yes' if so): ").lower()
while (ready != "yes"):
    ready = input(
        "Come on pussy, LET'S GO! Are you ready?! (Type 'yes' if so): ").lower()

print()
print()

# Play games
# Returns number of wins each and overall winner as tuple
winning_info = play_games(needed_wins, choices)

print_winner(winning_info)
