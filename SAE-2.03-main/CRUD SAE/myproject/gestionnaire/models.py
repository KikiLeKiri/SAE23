from django.db import models

# Create your models here.

class Etudiant(models.Model):
    numero_etudiant = models.IntegerField(unique=True,null=True, blank=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    groupe = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="gestionnaire/photo/",null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        managed = True
        db_table = 'Etudiant'

class UnitesEnseignement(models.Model):
    code = models.CharField(unique = True, max_length=100)
    nom = models.TextField()
    semestre = models.IntegerField()
    credit_ects = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'UnitesEnseignement'

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        managed = True
        db_table = 'Enseignant'
    
class Examen(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateField()
    coefficient = models.IntegerField()

    def __str__(self):
        return f"{self.titre}"

    class Meta:
        managed = True
        db_table = 'Examen'

class RessourcesUE(models.Model):
    code_ressource = models.CharField(unique= True, max_length=50)
    nom = models.TextField()
    descriptif = models.TextField()
    coefficient = models.IntegerField()

    def __str__(self):
        return self.nom
    
    class Meta:
        managed = True
        db_table = 'RessourcesUE'

class Note(models.Model):
    examen = models.ForeignKey('gestionnaire.Examen', on_delete=models.CASCADE)
    etudiant = models.ForeignKey('gestionnaire.Etudiant', on_delete=models.CASCADE)
    note = models.FloatField()
    appreciation = models.TextField()

    def __str__(self):
        return f"Note {self.pk}: {self.note} - {self.etudiant} - {self.examen}"

    class Meta:
        managed = True
        db_table = 'Note'
    




