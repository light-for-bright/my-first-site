from django.contrib import admin
from note_app import models

# Register your models here.
admin.site.register(models.Topic)
admin.site.register(models.Entry)
