from django.db import models

# Create your models here.

class Project(models.Model):
    Username = models.TextField()
    Classname = models.TextField()
    Projname = models.TextField()
    Description = models.TextField()
    contact_id = models.TextField()

    def __str__(self):
        return f"{self.Username}, {self.Classname}: {self.Projname}"
