from django.db import models


class MagicWord(models.Model):

    password = models.CharField(max_length=32, unique=True)
    is_enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ('password',)

    def __unicode__(self):
        return self.password
