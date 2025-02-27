from rest_framework import serializers
from .models import Student


# shorthand code using ModelSerializer

class serial(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']


    
     # field level validation

    def validate_roll(self, value):
        if value >= 100:
            raise serializers.ValidationError('No More Seat')
        return value
        

    # Object Level validation    
    def validate(self, data):
        nm = data.get('name')
        ct =  data.get('city')
        if nm.lower()=='lala' and ct.lower()!='butwal':
            raise serializers.ValidationError('Person must be of butwal')
        return data
    
    #validator
    def start_with_r(value):
     if value[0].lower()!='r':
        raise serializers.ValidationError('Name should start with r')

# class serial(serializers.Serializer):
#     name = serializers.CharField()
#     # name = serializers.CharField(validators =[start_with_r] )
#     roll = serializers.IntegerField()
#     city = serializers.CharField()
    
#     def create(self,validate_data):
#         return Student.objects.create(**validate_data)
    
#     def update(self,instance,validated_data):
#         instance.name= validated_data.get('name',instance.name)
#         instance.roll= validated_data.get('roll',instance.roll)
#         instance.city= validated_data.get('city',instance.city)
#         instance.save()
#         return instance
    
   