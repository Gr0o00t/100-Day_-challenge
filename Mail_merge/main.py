with open("./Input/Letters/starting_letter.txt", mode='r') as starting_letter:
    letter = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    for name in names:
        stripped=name.strip()
        letter = letter.replace("[name]", stripped)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped}.txt", mode='w') as file:
            file.write(letter)