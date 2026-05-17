from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from django.conf import settings
from common.models import SoftDeletionModel



class Topic(SoftDeletionModel):
    name = models.CharField(
        max_length=80
    )

    description = models.TextField()

    color = models.CharField(
        max_length=7,
        validators=[RegexValidator(regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'),
                    MinLengthValidator(4)]
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='topics'
    )

    def __str__(self):
        return f'{self.name[:30]}{"..." if len(self.name) > 30 else ""}'