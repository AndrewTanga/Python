love_array = ['TRUE', 'FOREVER']

limits = {
    "bottom": 11,
    "top": 89,
    "mid_bottom": 40,
    "mid_top": 50
}

def getLoversNames(number_of_lovers):
    names_array = []
    for i in range(number_of_lovers):
        full_name = input(f"Enter name {i+1} :")
        names_array.append(full_name.lower())
    names_string = ''.join(names_array)

    return list(names_string)

names_in_letters_array = getLoversNames(2)

def getScore():
    total_score = 0
    for word in love_array:
        word_score = 0
        word_letters_array = list(word.lower())
        letter_count = 0

        for letter in word_letters_array:
            letter_count = names_in_letters_array.count(letter)
            word_score += letter_count
        total_score += word_score

    return total_score

score = getScore()

if score < limits['bottom'] or score > limits['top']:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= limits['mid_bottom'] and score <= limits['mid_top']:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")