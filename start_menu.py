from csv_edit import CSVEditor
from pretty_prints import PrettyPrints
from user import User

class StartMenu():
    def __init__(self) -> None:
        self.pretty_prints = PrettyPrints()
        self.csvedit = CSVEditor()
        self.user = None

    def loginMenu(self):
        print(self.pretty_prints.welcome)
        print(self.pretty_prints.loginmenu)
        self.promptUser()

    def promptUser(self):
        while True:
            cmd = input("Enter choice: ")
            if cmd == "1":
                return self.login()
            elif cmd == "2":
                return self.createUser()
            else:
                print("Invalid choice!")

    def login(self):
        quit = ""
        while quit != "q":
            id = input("Enter your id: ")
            users = self.csvedit.get_info()
            for i in users:
                if i.id == id:
                    self.user = i
                    return
            quit = input("Id not found, press enter to continue or 'q' to quit")

    def createUser(self):
        username = input("Enter your name: ")
        id = hash(username.lower())//1000000000
        if id < 0:
            id *= -1
        self.user = User(id, username)
        print(self.pretty_prints.login_confirm.format(id))
        self.csvedit.write(self.user)

