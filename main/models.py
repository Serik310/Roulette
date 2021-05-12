from django.db import models
from user.models import CustomUser


class BetHistory(models.Model):
    winning_number = models.IntegerField('Winning number')
    created_at = models.DateTimeField('Created at', auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
