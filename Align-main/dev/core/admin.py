from django.contrib import admin
from .models import File, Tag, Project, Action

align_models = [File, Tag, Project, Action]
# Register your models here.
admin.site.register(align_models)

