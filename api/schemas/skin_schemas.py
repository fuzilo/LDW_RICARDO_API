from api import ma
from marshmallow import Schema, fields

class SkinSchema(ma.Schema):
    class Meta:
        fields=("_id", "name", "hero", "value")
    
    _id = fields.Str()
    name = fields.Str(required= True)
    hero = fields.Str(required= True)
    value = fields.Str(required= True)    