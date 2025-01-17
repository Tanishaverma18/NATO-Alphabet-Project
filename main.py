import pandas

data = pandas.read_csv("alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

word = input("Enter a word: ").upper()
try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, on;y letters in the alphabet please")
else:
    print(output_list)