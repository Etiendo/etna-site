from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


DESCRIPTION_TYPES = [
    ('RESTAURANT', 'RESTAURANT'),
    ('TAPAS', 'TAPAS'),
    ('WINE', 'VINS'),
]


class TapasCourse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)])
    comments = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{} à {}'.format(self.name, self.price)


class PresentationText(models.Model):
    text_type = models.CharField(max_length=100, choices=DESCRIPTION_TYPES)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return 'Le texte sur {} nommé {}'.format(self.text_type, self.title)
