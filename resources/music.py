from flask import Response, request
from database.models import Music
from flask_restful import Resource

class MusicsApi(Resource):
    def get(self):
        musics = Music.objects().to_json()
        return Response(musics, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        music =  Music(**body).save()
        id = music.id
        return {'id': str(id)}, 200
        
class MusicApi(Resource):
    def put(self, id):
        body = request.get_json()
        Music.objects.get(id=id).update(**body)
        return '', 200
    
    def delete(self, id):
        music = Music.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        musics = Music.objects.get(id=id).to_json()
        return Response(musics, mimetype="application/json", status=200)
