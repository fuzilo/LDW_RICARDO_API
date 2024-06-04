from api import mongo
from ..models import skin_model
from bson import ObjectId #Usado para ler objetos do Mongo

## O sérvice Contém os métodos de manipulação do banco de dados

def add_skin(skin):
    mongo.db.leagueOfSkins.insert_one({
        'name':skin.name,
        'hero':skin.hero,
        'value':skin.value
    })
    
@staticmethod
def get_skins():
    return list(mongo.db.leagueOfSkins.find())

@staticmethod
def get_skin_by_id(id):
    return mongo.db.leagueOfSkins.find_one({'_id': ObjectId(id)})

@staticmethod
def update_skin(self, id):
    mongo.db.leagueOfSkins.update_one({'_id': ObjectId(id)},
                              {'$set':
                                  {
                                      'name': self.name,
                                      'hero':self.hero,
                                      'value': self.value
                                  }})

@staticmethod
def delete_skin(id):
    mongo.db.leagueOfSkins.delete_one({'_id': ObjectId(id)})