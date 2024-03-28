from typing import Any
from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    url = models.URLField()
    short_url = models.URLField(unique=True)
    id_short = models.CharField(max_length=15)

    def __str__(self):
        return self.url

class Statistics(models.Model):
    id_short = models.ForeignKey(ShortUrl, on_delete=models.CASCADE)
    number_visits = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.id_short.__str__()
