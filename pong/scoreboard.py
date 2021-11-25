from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self, position, player):
        super().__init__()
        self.score = 0
        self.color('white')
        self.pu()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard(player)

    def update_scoreboard(self, player):
        self.clear()
        self.write(f"{player} score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        self.score += 1
        self.update_scoreboard(player)

    def game_over(self, winner):
        self.goto(0, 20)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -20)
        self.write(f"{winner} player won!", align=ALIGNMENT, font=FONT)