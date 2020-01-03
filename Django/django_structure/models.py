from django.db import models

class Django_Structure(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Files(models.Model):
    framework = models.CharField(max_length=72)
    folder = models.CharField(max_length=72)
    file = models.CharField(max_length=72)

    def __str__(self):
        return self.file