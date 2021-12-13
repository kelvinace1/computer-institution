from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from users.models import CustomUser

# Create your models here.
class Course(models.Model):
    total = models.IntegerField()
    general_computing = models.DecimalField(max_digits=5, decimal_places=2)
    operating_system = models.DecimalField(max_digits=5, decimal_places=2)
    ms_excel = models.DecimalField(max_digits=5, decimal_places=2)
    word_processing = models.DecimalField(max_digits=5, decimal_places=2)
    presentation = models.DecimalField(max_digits=5, decimal_places=2)
    corel_draw = models.DecimalField(max_digits=5, decimal_places=2)
    adobe_photoshop = models.DecimalField(max_digits=5, decimal_places=2)
    data_processing = models.DecimalField(max_digits=5, decimal_places=2)
    networking = models.DecimalField(max_digits=5, decimal_places=2)
    information_technology = models.DecimalField(max_digits=5, decimal_places=2)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.networking

    def get_absolute_url(self,**kwargs):
        return reverse('detail', kwargs={'pk':self.pk})

