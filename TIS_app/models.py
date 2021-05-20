from location_field.models.plain import PlainLocationField

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Comment(models.Model):
    description = models.TextField()


class Species(models.Model):
    name = models.CharField(max_length=64)
    latin_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} / {self.latin_name}"


class Inventory(models.Model):
    name = models.CharField(max_length=64)
    location = PlainLocationField()
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    principal = models.CharField(max_length=64)
    principal_address = models.CharField(max_length=128, null=True, blank=True)
    comments = models.ForeignKey(
        Comment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    def __str__(self):
        return f"""{self.pk}/{self.name}"""


class Circuit(models.Model):
    value = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(600)])


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
    circuit = models.ForeignKey(Circuit, on_delete=models.PROTECT)
    height = models.PositiveIntegerField()
    crown_width = models.PositiveIntegerField()
    roloff = models.PositiveIntegerField(
        choices=ROLOFF_CHOICES,
        default=ROLOFF_CHOICES[0])
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    def __str__(self):
        return f"""ID: {self.pk}, 
        inwentaryzacja: {self.inventory.name}, 
        numer identyfikacyjny drzewa: {self.identification_number},
        gatunek: {self.species.name} ({self.species.latin_name})"""


class Photo(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
