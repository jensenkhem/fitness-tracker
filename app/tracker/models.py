from django.db import models

# Create a sample model for the fitness tracker
# Not sure if this is the best solution yet, just getting something out there
class Exercise(models.Model):
    # Attributes
    name = models.CharField("Name", max_length=200)
    pub_date = models.DateTimeField("Date Published")
    reps = models.IntegerField("Reps")

    # Str representation
    def __str__(self):
        return "{name: " + self.name + ", reps: " + str(self.reps) + "}"


