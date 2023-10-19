from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from django.middleware import csrf

from .models import Projets, Blog, Compétences, Contact , Experience , Education
from .serliazers import ProjetsSerializer, BlogSerializer, CompétencesSerializer, ContactSerializer , UserSerializer , ExperienceSerializer , EducationSerializer




class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
def login_view(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)  
                return JsonResponse({'message': 'Login successful', 'token': token.key})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        
    
        return HttpResponse("Only POST requests are allowed", status=405)

# For Projets
class ProjetsListCreateView(generics.ListCreateAPIView):
    queryset = Projets.objects.all()
    serializer_class = ProjetsSerializer

    

class ProjetsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projets.objects.all()
    serializer_class = ProjetsSerializer

# For Blog
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# For Compétences
class CompétencesListCreateView(generics.ListCreateAPIView):
    queryset = Compétences.objects.all()
    serializer_class = CompétencesSerializer

class CompétencesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compétences.objects.all()
    serializer_class = CompétencesSerializer

# For Contact
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ExperienceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class EducationListCreateView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer






