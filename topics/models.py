from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from django.conf import settings
from common.models import SoftDeletionModel, BaseModel


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


class Resource(BaseModel):
    class TypeChoose(models.TextChoices):
        VIDEO = 'video', 'Video'
        ARTICLE = 'article', 'Article'
        BOOK = 'book', 'Book'
        OTHER = 'other', 'Other'

    class StatusChoose(models.IntegerChoices):
        NOT_STARTED = 0, 'Not Started'
        IN_PROGRESS = 1, 'In Progress'
        DONE = 2, 'Done'

    title = models.CharField(max_length=100)
    url = models.URLField()
    type = models.CharField(max_length=30, choices=TypeChoose, default=TypeChoose.OTHER)
    status = models.SmallIntegerField(choices=StatusChoose, default=StatusChoose.NOT_STARTED)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='resources')


    def __str__(self):
        return f'{self.title} - {self.status}'