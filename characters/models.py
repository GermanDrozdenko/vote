from django.db import models


class Character(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    img_url = models.ImageField(upload_to='images/')
    age = models.IntegerField()
    bio = models.TextField(max_length=850)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'
