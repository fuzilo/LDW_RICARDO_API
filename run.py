from api import app, mongo
from api.models.skin_model import LeagueOfSkins
from api.services import skin_service


if __name__ == "__main__":
    with app.app_context():
        if 'leagueOfSkins' not in mongo.db.list_collection_names():
            skin=LeagueOfSkins(
                name='',
                hero='',
                value='0'
            )
            skin_service.add_skin(skin)
    
    
    app.run(debug=True)
    
#app.run(host='localhost', port=5000, debug=True) -  para mudar a porta