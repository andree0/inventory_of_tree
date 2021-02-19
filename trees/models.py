from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Species(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Variant(models.Model):
    name = models.CharField(max_length=64)
    id_species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='species')

    def __str__(self):
        return f"{self.id_species.name} {self.name}"


class Tree(models.Model):
    ROLOFF_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    circuit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])
    roloff = models.IntegerField(choices=ROLOFF_CHOICES)
    hollow = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.species.name} {self.variant.name}"
