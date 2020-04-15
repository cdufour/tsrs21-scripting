# dictionary.py
# Comme la liste, ou le tuple, le dictionary est un type
# de donnée complexe

students = {} # création d'un dico vide
print(type(students)) # <class 'dict'>

fruit = {"name":"Pomme", "variety":"Golden"}
print(fruit["name"])

player1 = {
    "firstname":"Cristiano",
    "lastname":"Ronaldo",
    "num": 7,
    "team": "Juventus",
    "salary": 4000.50,
    "retired": False
}

player2 = {
    "firstname":"Lionel",
    "lastname":"Messi",
    "num": 10,
    "team": "Barcelone",
    "salary": 6000.50,
    "retired": False
}

player3 = {
    "firstname":"Roberto",
    "lastname":"Baggio",
    "num": 10,
    "team": "Juventus",
    "salary": 0,
    "retired": True
}
# print(player1["lastname"], "est un joueur de", player1["team"])
# print(player2["lastname"], "est un joueur de", player2["team"])

# liste de joueurs
players = [player1, player2, player3]
for player in players:
    if player["retired"] == True:
        print(player["lastname"], "était un joueur de", player["team"])
    else:
        print(player["lastname"], "est un joueur de", player["team"])