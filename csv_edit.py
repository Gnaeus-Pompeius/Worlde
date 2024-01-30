import csv
from user import User

class CSVEditor:
    def __init__(self) -> None:
        self.filename = "users.csv"

    def write(self, user):
        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ["id","username","highscores","wins","losses"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'id':user.id, "username":user.username, "highscores":":".join(sorted(user.highscores)), "wins":user.wins, "losses":user.losses})

    def get_info(self):
        ret_lis = []
        with open(self.filename, newline='', encoding='utf-8') as cvsfile:
            reader = csv.DictReader(cvsfile) #les inn skrána
            for row in reader:
                user = User(row["id"], row["username"], row["highscores"].split(":"), int(row["wins"]), int(row["losses"]))
                ret_lis.append(user)
            return ret_lis

    def updateFile(self, user):
        users = self.get_info()
        self.clearFile()
        user_found = False
        for i in users:
            if user.id == i.id:
                i = user
                user_found = True
            self.write(i)
        if not user_found:
            return "Could not save profile!"
        
    def clearFile(self):
        f = open(self.filename, "w", newline="")
        f.truncate()
        writer = csv.DictWriter(f, fieldnames = ["id","username","highscores","wins","losses"])
        writer.writeheader()
        f.close()