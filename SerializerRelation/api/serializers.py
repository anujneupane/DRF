from rest_framework import serializers
from .models import Song, Singer

class SingerSerial(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many = True, read_only = True)
    song = serializers.HyperlinkedRelatedField(many = True, read_only = True,view_name = 'song-detail')
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']

class SongSerial(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']  