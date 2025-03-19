from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, related_name='song',on_delete=models.CASCADE)  
    duration = models.IntegerField()  

    def __str__(self):
       return self.title

