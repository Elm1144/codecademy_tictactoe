# This will be my first project for codecademy

gameBoardDict = {
    "posOne": "1",
    "posTwo": "2",
    "posThree": "3",
    "posFour": "4",
    "posFive": "5",
    "posSix": "6",
    "posSeven": "7",
    "posEight": "8",
    "posNine": "9"
}

class Player:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter


def printGameboard(gameState):
    if gameState == "start":
        print("1 | 2 | 3")
        print("-   -   -")
        print("4 | 5 | 6")
        print("-   -   -")
        print("7 | 8 | 9")
    else:
        print("{} | {} | {}".format(gameBoardDict["posOne"], gameBoardDict["posTwo"], gameBoardDict["posThree"]))
        print("-   -   -")
        print("{} | {} | {}".format(gameBoardDict["posFour"], gameBoardDict["posFive"], gameBoardDict["posSix"]))
        print("-   -   -")
        print("{} | {} | {}".format(gameBoardDict["posSeven"], gameBoardDict["posEight"], gameBoardDict["posNine"]))

def wincondition():
    won = False
    # Waagerecht
    if (gameBoardDict["posOne"] == gameBoardDict["posTwo"] == gameBoardDict["posThree"]) or \
        (gameBoardDict["posFour"] == gameBoardDict["posFive"] == gameBoardDict["posSix"]) or \
        (gameBoardDict["posSeven"] == gameBoardDict["posEight"] == gameBoardDict["posNine"]):
        won = True
    # Senkrecht
    elif (gameBoardDict["posOne"] == gameBoardDict["posFour"] == gameBoardDict["posSeven"]) or \
        (gameBoardDict["posTwo"] == gameBoardDict["posFive"] == gameBoardDict["posEight"]) or \
        (gameBoardDict["posThree"] == gameBoardDict["posSix"] == gameBoardDict["posNine"]):
        won = True
    #Diagonal
    elif (gameBoardDict["posOne"] == gameBoardDict["posFive"] == gameBoardDict["posNine"]) or \
        (gameBoardDict["posThree"] == gameBoardDict["posFive"] == gameBoardDict["posSeven"]):
        won = True


    return won

def choosePosition(player, pos):
    pos = int(pos)
    if pos == 1:
        gameBoardDict["posOne"] = player.letter
    elif pos == 2:
        gameBoardDict["posTwo"] = player.letter
    elif pos == 3:
        gameBoardDict["posThree"] = player.letter
    elif pos == 4:
        gameBoardDict["posFour"] = player.letter
    elif pos == 5:
        gameBoardDict["posFive"] = player.letter
    elif pos == 6:
        gameBoardDict["posSix"] = player.letter
    elif pos == 7:
        gameBoardDict["posSeven"] = player.letter
    elif pos == 8:
        gameBoardDict["posEight"] = player.letter
    elif pos == 9:
        gameBoardDict["posNine"] = player.letter


print("!!!!!!!!!!!!!!!!!!!!!!!!")
print("Welcome to Tic Tac Toe!")
print("!!!!!!!!!!!!!!!!!!!!!!!!")
playerOneName = input("Please type in Player One's name ")
playerOne = Player(playerOneName, "x")
print("Welcome " + playerOne.name + ", your letter is: " + playerOne.letter)
playerTwoName = input("Please type in Player One's name ")
playerTwo = Player(playerTwoName, "o")
print("Welcome " + playerTwo.name + ", your letter is: " + playerTwo.letter)

print("\n This is how the gameboard looks like:")
printGameboard("start")

print("\n Now let's start")
printGameboard("game")
print("\n\n\n")

count = 1
while count < 9:
     inp = input(playerOne.name + " , please choose a number!\n")
     choosePosition(playerOne, inp)
     printGameboard("game")
     print("\n")
     if wincondition() == True:
        print(playerOne.name + " won the Game!!")
        exit()
     inp = input(playerTwo.name + " , please choose a number!")
     choosePosition(playerTwo, inp)
     printGameboard("game")
     if wincondition() == True:
        print(playerTwo.name + " won the Game!!")
        exit()
