from django.db import models

class MagicWord(models.Model):
    password = models.CharField(max_length=32)
    enabled = models.BooleanField()
    def __unicode__(self):
        return self.password