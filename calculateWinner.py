"""
Calculate the winner of a game of rock paper scissors.
Method name is the player's choice.
Return the winner.
"""


def rock(computer):
    if (computer == "Scissors"):
        return "player"
    elif (computer == "Paper"):
        return "computer"
    else:
        return "tie"


def paper(computer):
    if (computer == "Rock"):
        return "player"
    elif (computer == "Scissors"):
        return "computer"
    else:
        return "tie"


def scissors(computer):
    if (computer == "Paper"):
        return "player"
    elif (computer == "Rock"):
        return "computer"
    else:
        return "tie"
