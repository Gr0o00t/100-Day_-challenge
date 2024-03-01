alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

def ceaser ( start_text, shift_amount, chiper_direct):
    end_text=""
    if chiper_direct=="DECODE":
        shift_amount *=-1

    for char in start_text:
        if char in alphabet:
            position= alphabet.index(char)
            new_position= position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"Here's the {chiper_direct}d result {end_text}")

should_end=False
while not should_end:
    direction=input("Type encode or decode").upper()
    text=input("Type your message").upper()
    shift=int(input("Type the shift number"))

    shift=shift%26

    ceaser(text,shift,direction)
    restart= input("Type YES if you want to go again. Otherwise type NO. ").upper()
    if restart=="NO":
        should_end="True"
        print("Good Bye")