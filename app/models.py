from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_date(date):
         if date < timezone.now().date():
            raise ValidationError("Date cannot be in the past")

class events(models.Model):

    host = models.ForeignKey(
        User, on_delete=models.CASCADE, default='request.user', related_name='users')
    event_name = models.CharField(max_length=100)
    date = models.DateField(null=True,validators=[validate_date])
    time = models.TimeField(null=True)
    invited_user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.event_name

    

    


class invited(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    event = models.ForeignKey(
        events, on_delete=models.CASCADE, related_name='event')
