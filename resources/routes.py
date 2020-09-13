from .music import MusicsApi, MusicApi

def initialize_routes(api):
    api.add_resource(MusicsApi, '/musics')
    api.add_resource(MusicApi, '/musics/<id>')
