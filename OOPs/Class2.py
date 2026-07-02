class FootballPlayer:
    def __init__(self,name,jersey_number,contry):
        self.name=name
        self.jersey_number=jersey_number
        self.contry=contry

player1=FootballPlayer("Neymar",10,"Brazil")
player2 = FootballPlayer("Messi", 10, "Argentina")

print(player1.name)
print(player1.jersey_number)
print(player2.contry)