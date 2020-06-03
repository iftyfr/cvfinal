from django.db import models


class contactme(models.Model):
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    message = models.CharField(max_length=10000)

    def __str__(self):
        return self.message