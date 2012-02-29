from django.db import models


class Zombie(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    graveyard = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Tweet(models.Model):
    zombie = models.ForeignKey('Zombie', related_name='tweets')
    message = models.CharField(max_length=140)

    def __unicode__(self):
        return self.message
