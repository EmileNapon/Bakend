import datetime
from django.db import models
from datetime import date
from Formation.models import Module
from users.models import CustomUser


class Formation(models.Model):
    titre=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    type = models.TextField(max_length=200,null=True)
    niveau = models.CharField(max_length=800,null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Utilisation d'un DecimalField pour le prix
    duree = models.CharField(max_length=20)
    nombre = models.IntegerField(null=True)
    localisation = models.CharField(max_length=200,default='FIDALLI')
    resume=models.TextField(null=True)
    description=models.TextField(max_length=800)
 

class Group(models.Model):
    # Vous pouvez ajouter d'autres champs pertinents ici
    pass  # Remplacez-le par les champs appropriés pour votre groupe

class Inscrit(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)  # Relation vers Formation
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Relation vers Formation
    date = models.DateField(default=date.today)
    ##group = models.ForeignKey(Group, on_delete=models.CASCADE)  # À remplacer par un ForeignKey vers Group si applicable
    phone_number=models.TextField(max_length=20, default='')
    domaine_etude=models.TextField(max_length=40, default='')
    niveau_etude=models.TextField(max_length=100, default='')
    class Meta:
        unique_together = ('formation', 'user')  # Assure qu'un utilisateur ne peut s'inscrire qu'une seule fois à une formation
    def __str__(self):
        return f"{self.user} inscrit à {self.formation}"


class ModuleFormation(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)  # Relation vers Module
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)  # Relation vers Formation



class Encadrant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, default=1)
    domaine_expertise = models.CharField(max_length=20, default='null')
    fonction = models.CharField(max_length=50, default='null')

    def __str__(self):
        return f"{self.fonction} - {self.domaine_expertise}"

class Seance(models.Model):
    lieu = models.CharField(max_length=200)  # Renommé en CharField pour la localisation
    date_formation = models.DateField(default=date(2024, 1, 20))
    heure_debut = models.TimeField()  # Utilisation de TimeField pour les heures
    heure_fin= models.TimeField(null=True)
    statut = models.CharField(max_length=10, choices=[('confirmé', 'confirmé'),('annulé', 'annulé'),('attente', 'attente')], default='attente')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, default=1)  # Relation vers Module
    formation= models.ForeignKey(Formation, on_delete=models.CASCADE, default=1)  # Relation vers Module
    encadrant=models.ForeignKey(Encadrant, on_delete=models.CASCADE, default=1)

    
class AffectationStage(models.Model):
    inscrit = models.ForeignKey(Inscrit, on_delete=models.CASCADE)  # Relation vers Inscrit
   ## offre = models.ForeignKey(Offre, on_delete=models.CASCADE, default=1)  # Relation vers Inscrit
    date_affectation = models.DateField(default=date.today)
    group=models.ForeignKey(Group,on_delete=models.CASCADE, null=True)

########################################################################################



class Annonce(models.Model):
    titre = models.CharField(max_length=255)  # Titre de l'annonce
    lieu = models.CharField(max_length=255)   # Lieu de l'évènement
    date_cours = models.DateField()           # Date de l'évènement
    description = models.TextField()          # Description de l'annonce
    date_publication = models.DateField(default=date.today)  # Date de publication automatique
    heure = models.DateField(default=date.today)                # Heure de publication

    def __str__(self):
        return self.titre


