from utils.general_model import GeneralModel
from django.contrib.auth import get_user_model
from django.db import models
from term.models import Term


class Session(GeneralModel):
    PRESENT = 'present'
    ABSENT = 'absent'
    ABSENTALLOWED = 'absenceallowed'
    CLASS_TYPE = (
        (PRESENT, "present"),
        (ABSENT, "absent"),
        (ABSENTALLOWED, "absenceallowed"),
    )

    type = models.CharField('type', choices=CLASS_TYPE, default=PRESENT, max_length=14)

    name = models.CharField('name session', max_length=250 , blank=True, null=True, default=None)

    description = models.TextField('description', blank=True, null=True, default=None)

    location =  models.CharField(max_length=250, blank=True, null=True, default=None)

    term = models.ForeignKey(Term, on_delete=models.SET_NULL, blank=True,
                             null=True, default=None, related_name='sessions')

    def __str__(self):
        return f'{self.name}'

