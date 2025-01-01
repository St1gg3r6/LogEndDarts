from django.contrib import admin
from .models import Seasons, Matches, Players, Games


# Register your models here.
admin.site.register(Seasons)
admin.site.register(Matches)
admin.site.register(Players)
admin.site.register(Games)
