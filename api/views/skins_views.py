from flask_restful import Resource
from api import api
from ..schemas import skin_schemas
from .. models import skin_model
from ..services import skin_service
from flask import make_response, jsonify, request


class SkinList(Resource):
    def get(self):
        skins = skin_service.get_skins()
        s = skin_schemas.SkinSchema(many=True)
        
        return make_response(g.jsonify(skins), 200)#código 200 (OK), requisição bem sucedida
    
    def post(self):
        s = skin_schemas.SkinSchema()
        validate = s.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400) #Codigo 400, BAD_REQUEST: Solicitação Inválida
        else:
            name = request.json["name"]
            hero = request.json["hero"]
            value = request.json["value"]
            
            new_skin = skin_model.LeagueOfSkins(name=name, 
                                                hero=hero,
                                                value=value)
            result = skin_service.add_skin(new_skin)
            res = s.jsonify(result)
            return make_response(res, 201)#Código 201, CREATED: criação bem sucedida
    
    
    
class SkinDetails(Resource):    
    def get(self,id):
        skin = skin_service.get_skin_by_id(id)
        if skin is None:
            return make_response(jsonify(("Nenhuma Skin não foi encontrada"),404))#Código 404, NOT FOUND: rescuso requisistado, não encontrado
        s=skin_schemas.SkinSchema()
        return make_response(s.jsonify(skin),200)
    
    def put(self,id):
        skin_bd = skin_service.get_skin_by_id(id)
        if skin_bd is None:
            return make_response(jsonify("Skin não encontrada"), 404)
        s = skin_schemas.SkinSchema()
        validate = s.validate(request.json)
        if validate:
            return make_response(jsonify(validate),404)
        else:
            name = request.json["name"]
            hero = request.json["hero"]
            value = request.json["value"]
            new_skin = skin_model.LeagueOfSkins(name = name,
                                                hero = hero,
                                                value= value)
            skin_service.update_skin(new_skin, id)
            updated_skin = skin_service.get_skin_by_id(id)
            return make_response(g.jsonify(updated_skin),200)
    
    def delete(self, id):                    
        skin_bd = skin_service.get_skin_by_id(id)
        if skin_bd is None:
            return make_response(jsonify("Skin não encontrada"), 404)
        skin_service.delete_skin(id)
        return make_response(jsonify(" =( Skin Excluída com sucesso!", 204))#NO CONTENT, indica que a requisição foi bem sucedida, mas não há conteúdo para ser exibido
        

api.add_resource(SkinList, '/leagueofskins')    
api.add_resource(SkinDetails, '/leagueofskins/<id>')    

