from django.db import models

# Create your models here.


class Imager(models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField(upload_to='media')
    date=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return "{} - {}".format(self.title, self.image)