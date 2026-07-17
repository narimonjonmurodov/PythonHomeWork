# Assignment Tasks

## 1. Number Guess Game [LINK](Task1.py)
- Generate a random number between 0 and 100.
- Ask the user to guess the number.
- If the guess is too low, display "Go higher."
- If the guess is too high, display "Go lower."
- Continue asking until the correct number is guessed.
- When the user guesses correctly, display the total number of attempts.

## 2. Rock Paper Scissors [LINK](Task2.py)
- Play against the computer.
- The computer chooses Rock, Paper, or Scissors randomly.
- The user enters Rock, Paper, or Scissors.
- If the user enters an invalid value, ask again and do not count the round.
- Continue playing until either the user or the computer wins 3 rounds.
- Display the winner when the game ends.

## 3. Word Guess Game [LINK](Task3.py)
- Store a list of words.
- The computer randomly selects one word.
- Display the word as underscores (_), one for each letter.
- The user guesses one letter at a time.
- If the letter exists, reveal all matching positions.
- If the letter does not exist, decrease the remaining attempts.
- The user has 8 attempts.
- The user wins by revealing the entire word before running out of attempts.
- The user loses if all 8 attempts are used before guessing the word.

## 4. Vending Machine
Products:
- Coffee: 150 TL
- Tea: 90 TL
- Hot Chocolate: 120 TL
- Cola: 80 TL
- Water: 50 TL

Initial Stock:
- 10 units for each product.

User Menu:
- View available products.
- Products with 0 stock must not be displayed.
- If all products are out of stock, display a message.
- Purchase products.
- A purchase is allowed only if:
  - The user has enough credit.
  - The product is in stock.
- The user can continue purchasing until they choose to stop.

Admin Menu:
- View report:
  - Remaining stock of all products.
  - Total money in the machine.
- Refill product stock:
  - Select a product.
  - Enter the quantity to add.
- Withdraw money from the machine.
- Display the remaining money after withdrawal.
- Exit.
- Switch from Admin mode to User mode.
- If a product is out of stock, ask whether to refill it.
