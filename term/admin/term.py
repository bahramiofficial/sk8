from django.contrib import admin
from term.models import Term



class TermAdmin(admin.ModelAdmin):
    model = Term




