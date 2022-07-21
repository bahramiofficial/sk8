from django.contrib import admin
from term.models import  Term, Session
from .session import SessionAdmin
from .term import TermAdmin

admin.site.register(Term, TermAdmin)
admin.site.register(Session, SessionAdmin)