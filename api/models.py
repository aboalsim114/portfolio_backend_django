from django.db import models



class Projets(models.Model):
    name = models.CharField(max_length=100, unique=True , null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True , null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title



class Compétences(models.Model):
    competence = models.CharField(max_length=100, unique=True , null=False, blank=False, default="JS")
    projet = models.ForeignKey(Projets, on_delete=models.CASCADE)





class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=100)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)



class Experience(models.Model):
    poste = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    contrat = models.CharField(max_length=100)
    data_commencement = models.DateField()
    lieu = models.CharField(max_length=100)
    image_entreprise = models.ImageField(upload_to='images', null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




class Education(models.Model):
    ecole = models.CharField(max_length=100)
    diplome = models.CharField(max_length=100)
    Domaine_etude = models.CharField(max_length=100)
    Date_debut = models.DateField()
    année_reussi = models.BooleanField(default=False) 
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    



