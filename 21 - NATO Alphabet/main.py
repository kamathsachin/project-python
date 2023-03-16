import pandas

phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}

user_input = input("Enter a word: ").upper()
phonetic_list = [phonetic_dict[alpha] for alpha in user_input]
print(phonetic_list)