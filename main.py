import turtle
import pandas

screen = turtle.Screen()
screen.title("Afghanistan Provinces Game")
image = "afghanistan-map.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("34_province.csv")
all_province = data["province"].to_list()
guessed_province = []

while len(guessed_province) < 34:

    answer_province = screen.textinput(title=f"{len(guessed_province)}/34 Province correct",
                                       prompt="What's another province's name?").title()

    if answer_province == "Exit":
        missing_province = [province for province in all_province if province not in guessed_province]
#         missing_province = []
#         for province in all_province:
#             if province not in guessed_province:
#                 missing_province.append(province)
        new_data = pandas.DataFrame(missing_province)
        new_data.to_csv("provinces_to_learn.csv")
        break
    if answer_province in all_province:
        guessed_province.append(answer_province)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.province == answer_province]
        t.goto(int(province_data.x), int(province_data.y))
        # t.write(state_data.state.item())
        t.write(answer_province)

screen.exitonclick()
