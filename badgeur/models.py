from django.db import models

# Create your models here.
class Badgeur(models.Model):
  '''
  un badgeur est une personne à qui on donne un badge.
  p16: au minimum nom, prénom, NIN
  optionel: mail, 2 N° de tel
  '''
  nom = models.CharField(max_length=150)
  prenom = models.CharField(max_length=150)
  nin = models.CharField(max_length=30) # N° identité national
  mail = models.CharField(max_length=150, null=True, blank=True)
  tel1 = models.CharField(max_length=30, null=True, blank=True)
  tel2 = models.CharField(max_length=30, null=True, blank=True)

class Badge(models.Model):
  badgeur = models.ForeignKey(Badgeur, on_delete=models.CASCADE)