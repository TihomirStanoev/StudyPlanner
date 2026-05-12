from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from accounts.validators import MaxYearValidator




class CustomUser(AbstractUser):
    birth_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxYearValidator()])