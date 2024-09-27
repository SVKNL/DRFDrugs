from django.db import models

# Create your models here.
class Drugs(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    group = models.ForeignKey('Groups', on_delete=models.PROTECT, null=True)
    photo = models.ImageField()

    def __str__(self):
        return self.title


class Groups(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name