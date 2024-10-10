import random

class Human:
    def __init__ (self, name):
        self.name = name
    
    def get_name (self):
        return self.name

class Player (Human):
    def set_team (self, team):
        self.team = team
    
    def get_team (self):
        return self.team

players_name = ["Hossein", "Maziar", "Akbar", "Nima", "Mahdi", "Farhad", "Mohammad", "khashayar", "Milad", "Mostafa", "Amin", "Saeed", "Poya", "Poria", "Reza", "Ali", "Behzad", "Soheil", "Behroz", "Shahroz", "Saman", "Mohsen"]

players = []

team_a_count = 0
team_b_count = 0

for i in range (22):
    a = random.randint (1, 10)
    p = Player (players_name[i])

    if (a % 2 == 0):
        if (team_a_count < 11):
            p.set_team ("A")
            team_a_count = team_a_count + 1
        else:
            p.set_team ("B")
            team_b_count = team_b_count + 1
    else:
        if (team_b_count < 11):
            p.set_team ("B")
            team_b_count = team_b_count + 1
        else:
            p.set_team ("A")
            team_a_count = team_a_count + 1
    
    players.append (p)

for i in range (22):
    print ("Name:", players[i].get_name (), "Team:", players[i].get_team ())
