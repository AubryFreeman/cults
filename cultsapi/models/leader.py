from django.db import models


class Leader(models.Model):
    name = models.CharField(max_length=100)
    aliases = models.JSONField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=100)
    date_of_death = models.DateField(null=True, blank=True)
    place_of_death = models.CharField(max_length=100, null=True, blank=True)
    family_background = models.TextField()
    education = models.TextField()
    cult_founded = models.CharField(max_length=100)
    founding_date = models.CharField(max_length=200)
    founding_location = models.CharField(max_length=100)
    core_beliefs = models.TextField()
    symbols = models.TextField()
    leadership_style = models.TextField()
    significant_events = models.TextField()
    controversies = models.TextField()
    followers = models.TextField()
    impact = models.TextField()
    media_coverage = models.TextField()
    personality_traits = models.TextField()
    mental_health = models.TextField(null=True, blank=True)
    criminal_record = models.TextField(null=True, blank=True)
    trials_and_sentences = models.TextField(null=True, blank=True)
    public_perception = models.TextField()
    influence_on_modern_movements = models.TextField()

    def __str__(self):
        return self.name
