from django.contrib import admin
from term.models import  Session


class SessionAdmin(admin.ModelAdmin):
    model = Session



