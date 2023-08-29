from rest_framework import serializers
from .models import Skill, Project, ProjectRating, Education

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'skills', 'num_of_ratings', 'avg_ratings']

class ProjectRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRating
        fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"