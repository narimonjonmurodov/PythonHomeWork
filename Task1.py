import random

randomNumber = random.randrange(1, 100)
attempts = 1
print(randomNumber)
while True:
    try:
        user_num = int(input("[Input only num between 1 to 100]Try to guess a number between 1 and 100: "))

        if user_num <1 or user_num >= 100:
            raise ValueError

        if user_num > randomNumber:
            print(">> [Go lower]")
        elif user_num < randomNumber:
            print("<< [Go higher]")
        else:
            print(f"The number was: [{randomNumber}]")
            print(f"Your attempts is [{attempts}]")
            print("You Win [Congratulations!!]")
            break

    except ValueError:
        print("Warning[ValueError]: Please enter a number between 1 and 100")

    finally:
        attempts += 1
