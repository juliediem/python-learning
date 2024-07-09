student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(key)
    print(value)
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(index)
    # print(row)
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
#
# #TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}
#
# new_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}
# print(new_dict)
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# input = input("What word do you want to convert?").upper()
# input_list = [letter for letter in input]
# print(input_list)
#
# phonetic_code =[new_dict[letter] for letter in input_list]
# print(phonetic_code)