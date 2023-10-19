from django.urls import path, include
from .views import *


urlpatterns = [
        path('login/', login_view, name='login'),
    path('api/users/', UserListView.as_view(), name='user-list'),
     path('api/register/', UserCreateView.as_view(), name='register'),
    path("api/Projets/", ProjetsListCreateView.as_view(), name="projets-list-create"),
    path("api/Projets/<int:pk>/", ProjetsRetrieveUpdateDestroyView.as_view(), name="projets-detail"),
    
    path("api/Blog/", BlogListCreateView.as_view(), name="blog-list-create"),
    path("api/Blog/<int:pk>/", BlogRetrieveUpdateDestroyView.as_view(), name="blog-detail"),
    
    path("api/Compétences/", CompétencesListCreateView.as_view(), name="competences-list-create"),
    path("api/Compétences/<int:pk>/", CompétencesRetrieveUpdateDestroyView.as_view(), name="competences-detail"),
    path("api/Education/", EducationListCreateView.as_view(), name="Education-list-create"),
    path("api/Education/<int:pk>/", EducationRetrieveUpdateDestroyView.as_view(), name="Education-detail"),
    path("api/Experience/", ExperienceListCreateView.as_view(), name="Experience-list-create"),
    path("api/Experience/<int:pk>/", ExperienceRetrieveUpdateDestroyView.as_view(), name="Experience-detail"),
    
    path("api/Contact/", ContactListCreateView.as_view(), name="contact-list-create"),
    path("api/Contact/<int:pk>/", ContactRetrieveUpdateDestroyView.as_view(), name="contact-detail"),
]
