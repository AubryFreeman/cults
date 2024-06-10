from django.db import models


class Cult(models.Model):
    name = models.CharField(max_length=255)
    founder = models.CharField(max_length=255)
    founding_date = models.DateField()
    location = models.TextField()
    symbols = models.TextField()
    core_beliefs = models.TextField()
    rituals_practices = models.TextField()
    hierarchy = models.TextField()
    membership = models.TextField()
    significant_events = models.TextField()
    public_perception = models.TextField()
    controversies = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
