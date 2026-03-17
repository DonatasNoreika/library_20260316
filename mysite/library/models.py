from django.db import models

class Author(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

