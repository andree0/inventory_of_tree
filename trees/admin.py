from django.contrib import admin

from .models import Tree, Species, Variant

# Register your models here.
admin.site.register(Tree)
admin.site.register(Species)
admin.site.register(Variant)