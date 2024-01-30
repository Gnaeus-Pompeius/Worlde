from pretty_prints import PrettyPrints

class User():
    def __init__(self, uid, uname, hscores = ["0"]*10, wins = 0, losses = 0) -> None:
        self.id = uid
        self.username = uname
        self.highscores = hscores
        self.wins = wins
        self.losses = losses

    def addToHighscore(self, score):
        temp = score
        for c, i in enumerate(self.highscores):
            if int(temp) > int(i):
                self.highscores[c] = str(temp)
                temp = i


    def __str__(self) -> str:
        return PrettyPrints().stats.format(self.wins, self.losses, " : ".join(self.highscores))