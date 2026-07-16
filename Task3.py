my_set = {
    "apple", "house", "water", "phone", "table",
    "chair", "window", "garden", "school", "friend",
    "family", "market", "street", "coffee", "orange",
    "summer", "winter", "flower", "bridge", "rabbit"
}

word = my_set.pop().upper().replace(" ", "")
rm_word = word
chances = 8

while True:
    remind_w = rm_word.replace("_", "") #reminded words
    if remind_w == "" or chances == 0:
        print("You Lost [Try again, if you want]") if chances == 0 else print("You Win [Congratulations;)]")
        break

    latter = input("Please enter a alphabetical latter of word: ").upper().replace(" ", "")

    if len(latter) != 1 or latter not in remind_w:
        chances -= 1

        print("Warning[amount of letter]: Please enter a latter") if len(latter) != 1 \
        else print("Warning[not alphabetical]: Please enter a alphabetical latter") \
        if not latter.isalpha() else print("Wrong, Please try again.")

        print(f"You left {chances} chances.")
        continue
    rm_word = rm_word.replace(latter, "_")

    for x in range(len(word)):
        print(word[x], end="") if rm_word[x] == "_" else print("_", end="")

    print() # for new line