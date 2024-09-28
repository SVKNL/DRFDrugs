from django.db import models


# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Drugs(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    group = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
