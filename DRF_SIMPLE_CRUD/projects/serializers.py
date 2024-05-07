from rest_framework import serializers
from .models import projects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)