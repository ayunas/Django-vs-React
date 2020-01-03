from django.db import models

class Django_Structure(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Files(models.Model):
    framework = models.CharField(max_length=72)
    name = models.CharField(max_length=72)
    is_file = models.BooleanField()
    parent_id = models.IntegerField(null=True)

    def __str__(self):
        return self.file