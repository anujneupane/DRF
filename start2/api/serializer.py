from rest_framework import serializers
from .models import Student


class serial(serializers.Serializer):
    name = serializers.CharField()
    roll = serializers.IntegerField()
    city = serializers.CharField()
    
    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        instance.name= validated_data.get('name',instance.name)
        instance.roll= validated_data.get('roll',instance.roll)
        instance.city= validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    # field level validation

    def validate_roll(self, value):
        if value >= 100:
            raise serializers.ValidationError('No More Seat')
        return value
        