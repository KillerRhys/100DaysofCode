""" American Top 50!
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.07.05-2013 """


import turtle
import pandas


display = turtle.Screen()
display.title('Stare State')
image = 'blank_states_img.gif'
display.addshape(image)
turtle.shape(image)
sin = turtle.Turtle()
sin.pu()
sin.hideturtle()
data = pandas.read_csv('50_states.csv')
score = 0
states = len(data)
game_over = False
guessed = []

# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
while not game_over:
    if score < 50:
        guess = display.textinput(title=f"Current Score: {score}/{states}", prompt="Guess a State: ").title()
        if guess == 'Exit':
            all_states = data.state.to_list()
            for item in guessed:
                all_states.remove(item)
            missed_states = pandas.DataFrame(all_states)
            missed_states.to_csv('missed_states.csv')
            break

        elif guess in data['state'].values:
            if guess not in guessed:
                score += 1
                guessed.append(guess)
                x = int(data['x'].where(data['state'] == guess).dropna().values)
                y = int(data['y'].where(data['state'] == guess).dropna().values)
                print(x, y)
                print(type(x))
                sin.goto(x, y)
                sin.write(guess)

    if score == 50:
        sin.home()
        sin.color('blue')
        sin.write(arg='You rock you got them all!', align='center', font=('Arial', 30, 'bold'))
