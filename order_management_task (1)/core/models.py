from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user_email = models.EmailField()

    def __str__(self):
        return self.title
