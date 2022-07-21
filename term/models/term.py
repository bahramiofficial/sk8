from utils.general_model import GeneralModel
from config.settings import AUTH_USER_MODEL
from django.db import models

class Term(GeneralModel):
    PRIVATE = 'private'
    SEMIPRIVATE = 'semiprivate'
    PUBLIC = 'public'
    CLASS_TYPE = (
        (PRIVATE, "private"),
        (SEMIPRIVATE, "semiprivate"),
        (PUBLIC, "public"),
    )
    active = models.BooleanField(default=True)
    type = models.CharField('type', choices=CLASS_TYPE, default=PRIVATE, max_length=11)
    name = models.CharField('name terms', max_length=250)
    description = models.TextField('description', blank=True, null=True, default=None)
    time = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

    end_at = models.DateTimeField(
        verbose_name='Created Time', blank=True, null=True, default=None
    )
    pay = models.BooleanField(default=False)
    
    maker = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              blank=True, null=True,
                              default=None,related_name='terms')

    # student = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'


