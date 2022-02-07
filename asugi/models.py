from django.db import models

class Persona(models.Model):
    tessera = models.CharField(max_length=20)
    positività = models.BooleanField()
    questionario = models.BooleanField()

    def __str__(self):
        return self.tessera
