from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Comment(models.Model):
    description = models.TextField()


class Species(models.Model):
    name = models.CharField(max_length=64)
    latin_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} / {self.latin_name}"


class Inventory(models.Model):
    name = models.CharField(max_length=64)
    localisation = models.CharField(max_length=128)
    term = models.DateField()
    employer = models.CharField(max_length=64)
    employer_address = models.CharField(max_length=128, null=True, blank=True)
    comments = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"""ID: {self.pk},
        nazwa: {self.name},
        lokalizacja: {self.localisation},
        termin: {self.term}"""


class Tree(models.Model):
    ROLOFF_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4')
    )
    identification_number = models.PositiveIntegerField()
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    circuit = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])
    roloff = models.PositiveIntegerField(choices=ROLOFF_CHOICES)
    hollow = models.BooleanField(default=False)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    def __str__(self):
        return f"""ID: {self.pk}, 
        inwentaryzacja: {self.inventory.name}, 
        numer identyfikacyjny drzewa: {self.identification_number},
        gatunek: {self.species.name} ({self.species.latin_name})"""


class Photo(models.Model):
    image = models.ImageField()
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
