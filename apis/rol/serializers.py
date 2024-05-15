from rest_framework import serializers
from .models import rol, desarrolador,tasks

class rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'
        
class desarroladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = desarrolador
        fields = '__all__'
        
class tasksSerializer(serializers.ModelSerializer):
    class Meta:
        model= tasks
        fields= '__all__'