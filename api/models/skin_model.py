from api import mongo

class LeagueOfSkins():
    def __init__(self, name, hero, value):
        self.name = name
        self.hero = hero
        self.value = value