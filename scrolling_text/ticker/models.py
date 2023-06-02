from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RunningTextHistory(models.Model):
    text = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
