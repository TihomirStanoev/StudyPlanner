from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import CASCADE

from common.models import BaseModel


class StudySession(BaseModel):
    topic = models.ForeignKey('topics.Topic', on_delete=CASCADE, related_name='study_sessions')
    date = models.DateTimeField()
    duration_minutes = models.SmallIntegerField(validators=[MinValueValidator(0)])
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.topic} - {self.date}'


class Goal(BaseModel):
    topic = models.ForeignKey('topics.Topic', on_delete=CASCADE, related_name='goals')
    target_minutes = models.SmallIntegerField(validators=[MinValueValidator(0)])
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.topic} - {self.is_completed}'

