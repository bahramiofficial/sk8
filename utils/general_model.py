from django.db import models


class GeneralModel(models.Model):
    create_at = models.DateTimeField(
        verbose_name='Created Time',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated Time',
        auto_now=True
    )

    delete = models.BooleanField(
        default=False
    )

    class Meta:
        abstract = True
