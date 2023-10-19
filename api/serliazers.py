from rest_framework import serializers
from .models import Projets , Blog , Compétences , Contact, Experience , Education
from django.contrib.auth.models import User


class ProjetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projets
        fields = '__all__'

    



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'




class CompétencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compétences
        fields = '__all__'



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}




class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'




class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'