from django.contrib import admin
from . import models


admin.site.register(models.Profile)
admin.site.register(models.Gamemodel)
admin.site.register(models.General)
admin.site.register(models.History)

