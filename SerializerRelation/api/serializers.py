from rest_framework import serializers
from .models import Song, Singer

class SongSerial(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration'] 

class SingerSerial(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many = True, read_only = True)
    #song = serializers.HyperlinkedRelatedField(many = True, read_only = True,view_name = 'song-detail')
    #song = serializers.SlugRelatedField(many = True, read_only = True,slug_field = 'duration')
    # song = serializers.HyperlinkedIdentityField(view_name = 'song-detail')
    song =SongSerial(many= True,read_only = True)
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']

 