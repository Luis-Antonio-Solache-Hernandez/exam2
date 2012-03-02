from django.db import models


class Zombie(models.Model):
    name = models.CharField(max_length=25)
    graveyard = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name


class Twitt(models.Model):
    status = models.CharField(max_length=140)
    zombie = models.ForeignKey(Zombie)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "By " + self.zombie.name + "at" + self.created_at

    class Meta:
        ordering = ['-created_at']
