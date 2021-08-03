from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        with open("day_24/snake_game/score_details.txt") as pre_high_scores:
            self.high_score=int(pre_high_scores.read())

        self.write(f"Score : {self.score} HighScore : {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))

    def update_score(self):
        
        self.clear()
        self.write(f"Score : {self.score} HighScore : {self.high_score}" , align="center",
                   font=("Arial", 24, "normal"))
    def increase_score(self):
        self.score+=1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day_24/snake_game/score_details.txt","w") as scores:
                scores.write(str(self.high_score))

        self.score=0
        self.update_score()

    # def game_over(self):

    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
