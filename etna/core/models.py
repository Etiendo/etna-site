from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


DESCRIPTION_TYPES = [
    ('RESTAURANT', 'RESTAURANT'),
    ('TAPAS', 'TAPAS'),
    ('WINE', 'VINS'),
]

LANGUAGES = [
  ('FR', 'FR'),
  ('EN', 'EN')
]


class Tapas(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    prix = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)])
    ordre = models.IntegerField(validators=[
                                MinValueValidator(0), MaxValueValidator(100)], default=1)
    commentaires = models.TextField(max_length=100, null=True, blank=True)
    langue = models.CharField(max_length=100, choices=LANGUAGES, default='FR')

    def __str__(self):
        return '{} à {}€, n°{}'.format(self.nom, self.prix, self.ordre)


class TexteDePresentation(models.Model):
    type_de_texte = models.CharField(max_length=100, choices=DESCRIPTION_TYPES)
    titre = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    langue = models.CharField(max_length=100, choices=LANGUAGES, default='FR')

    def __str__(self):
        return '{} : {} - {}'.format(self.type_de_texte, self.titre, self.langue)
