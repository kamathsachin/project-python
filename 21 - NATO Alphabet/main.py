import pandas

phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetic_dict[alpha] for alpha in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()
