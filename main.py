# Object-oriented programming
class BasketballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def weight_to_lbs(self):
        return round(self.weight_kg * 2.20462262, 2)

joze = BasketballPlayer(first_name="Jože", last_name="Novak", height_cm=178, weight_kg=85, points=26, rebounds=13.1, assists=3)
matic = BasketballPlayer(first_name="Matic", last_name="Derganc", height_cm=189, weight_kg=65, points=6, rebounds=3.1, assists=1)

bb_players = [joze, matic]

for player in bb_players:
    print(player.first_name + " " + player.last_name + ": " + str(player.weight_to_lbs()))
