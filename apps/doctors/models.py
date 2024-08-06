from django.contrib.auth.models import User
from django.db import models

from apps.utils.base_model import BaseModel


class Doctor(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_count = models.PositiveSmallIntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'doctors'
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'
