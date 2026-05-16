from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils import timezone




@deconstructible
class MaxYearValidator:
    def __init__(self):
        self.message = 'Year must not be in the future.'
        self.code = 'max_year'


    def __call__(self, value):
        current_year = timezone.now().year

        if value > current_year:
            raise  ValidationError(self.message, code=self.code, params={'value': value})

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.message == other.message and self.code == other.code

