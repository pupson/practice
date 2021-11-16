from hl_art import logo, vs
from hl_data import data

import random

# print logo

print(logo)

# access data list of dict randomly, print name description country of 1st choice
def rand_choice():
    
    ran_num = random.randint(0, len(data)-1)

    first_option = data[ran_num]
    first_option_name = first_option["name"]
    first_option_follower = first_option["follower_count"]
    first_option_desc = first_option["description"]
    first_option_ctry = first_option["country"]

    return first_option_name, first_option_follower, first_option_desc, first_option_ctry

game = True

while game == True:

    name, follow, desc, ctry = rand_choice()
    choice_dict = {}
    choice_dict['A'] = follow
    print(f"Compare A: {name}, {desc}, {ctry}")

    # print vs

    print(vs)

    # access data dict randomly, print name description country of 2nd choice

    name, follow, desc, ctry = rand_choice()
    choice_dict['B'] = follow
    print(f"To B: {name}, {desc}, {ctry}")

    guess = input(f'Who has more followers, A/B? ')

    if choice_dict['A'] > choice_dict['B']:
        choice_dict.pop('B')
    else:
        choice_dict.pop('A')

    for letter, count in choice_dict.items():
        if guess == letter:
            print("You're right!")
            game = True
        else:
            print("You're wrong")
            game = False