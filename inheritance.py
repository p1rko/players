import json

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


f_name = input("Player's name: ")
l_name = input("Player's last name: ")
age = input("Player's age: ")
height = float(input("Player's height in cm: "))
weight = float(input("Player's weight in kg: "))

type = input("Does he play basketball or football? ")

if type.lower() == "basketball":
    points = int(input("Number of points: "))
    rebounds = int(input("Number of rebounds: "))
    assists = int(input("Number of assists: "))

    new_player = BasketballPlayer(first_name=f_name, last_name=l_name, age=age, height_cm=height, weight_kg=weight, points=points, rebounds=rebounds, assists=assists)
    with open("players.json", "a") as players_file:
        players_file.write("Basketball player: " + str(new_player.__dict__))

    print("Player successfully entered!")
    print("Player's data: {0}".format(new_player.__dict__))

elif type.lower() == "football":
    goals = int(input("Number of goals: "))
    yellows = int(input("Number of yellow cards: "))
    reds = int(input("Number of red cards: "))

    new_player = FootballPlayer(first_name=f_name, last_name=l_name, age=age, height_cm=height, weight_kg=weight, goals=goals, yellow_cards=yellows, red_cards=reds)
    with open("players.json", "a") as players_file:
        players_file.write("Football player: " + str(new_player.__dict__))

    print("Player successfully entered!")
    print("Player's data: {0}".format(new_player.__dict__))

