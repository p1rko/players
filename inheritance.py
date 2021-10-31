class Player():
    def __init__(self, first_name, last_name, age, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        return round(self.weight_kg * 2.20462262, 2)

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, age, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, age=age, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assist = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, age, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, age=age, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

matic = BasketballPlayer(first_name="Matic", last_name="Derganc", age=21, height_cm=189, weight_kg=65, points=6, rebounds=3.1, assists=1)
leo = FootballPlayer(first_name="Leo", last_name="Velloti", age=17, height_cm=172, weight_kg=70, goals=12, yellow_cards=5, red_cards=2)


