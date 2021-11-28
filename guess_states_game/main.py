import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv('50_states.csv')
# print(states_data)
states_lst = states_data['state'].tolist()
print(states_lst)

guess_states = []
# game_is_on = True

while len(guess_states) < 50:
    guess = screen.textinput(title=(f'{len(guess_states)}/50 States Correct'), prompt='Input a state name:')
    guess = guess.title()

    if guess.lower() == 'exit':
        missed_states = []
        for state in states_lst:
            if state not in guess_states:
                missed_states.append(state)
        df = pandas.DataFrame(missed_states)
        df.to_csv('states_to_learn.csv')
        break
    elif guess in states_lst:

        correct_state = states_data[states_data['state'] == guess]
        guess_shape = turtle.Turtle()
        guess_shape.hideturtle()
        guess_shape.pu()
        guess_states.append(guess)
        guess_shape.goto(int(correct_state.x), int(correct_state.y))
        guess_shape.write(guess, font='Courier', align='center')
        # guess_shape.write(correct_state.state.item())

    # else:
    #     game_is_on = False
# print(states_data[correct_state[1]])
# guess_shape.goto(correct_state['x'], correct_state['y'])
# print()

# GET SCREEN COORDS FOR STATE X,Y
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
#
# screen.exitonclick()

