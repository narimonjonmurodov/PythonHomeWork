import random

userWins = computerWins = 0

moves = ["Rock", "Paper", "Scissor"]
moves = [move.upper() for move in moves]

while userWins != 3 and computerWins != 3:
    user = input("Please enter your choice: ").upper()

    if user not in moves:
        print("Please enter a valid move: [Rock] / [Paper] / [Scissor]")
        continue

    computer = random.choice(moves)

    if computer == user:
        print("Draw [Try again]")
        continue

    userIndex, computerIndex = moves.index(user), moves.index(computer)
    distance = abs(userIndex - computerIndex)

    if distance == 1:
        if userIndex < computerIndex:
            print(f"[{computer}] Win!")
            computerWins += 1
        else:
            print(f"[{user}] Win!")
            userWins += 1
    else:
        if userIndex > computerIndex:
            print(f"[{computer}] Win!")
            computerWins += 1
        else:
            print(f"[{user}] Win!")
            userWins += 1

    print(f"Computer[{computer}]: {computerWins}")
    print(f"You[{user}]: {userWins}")

if computerWins == 3:
    print(f"Computer Wins [Try again, if you want]")
else:
    print(f"You Win [Congratulations]")