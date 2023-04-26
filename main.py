import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
di = {row.letter: row.code for (index, row) in alphabet.iterrows()}
print(di)

def asker():
    word = input("Type name: ").upper()
    try:
        phonetic_code = [di[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        asker()
    else:
        print(phonetic_code)

asker()