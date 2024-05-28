import pandas as pd
name = input (" Please enter your name").upper()

aplha = pd.read_csv("nato_phonetic_alphabet.csv")

returna = { rows.letter:rows.code for (index,rows) in aplha.iterrows()}


output1 = [ returna[lette] for lette in name]

print (output)
