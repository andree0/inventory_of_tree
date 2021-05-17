# from allauth.socialaccount.models import SocialApp

from django.contrib import admin

from TIS_app.models import Circuit, Comment, Inventory, Photo, Species, Tree


@admin.register(Circuit)
class CircuitAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


# @admin.register(SocialApp)
# class SocialAppAdmin(admin.ModelAdmin):
#     pass


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    pass


@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    pass
