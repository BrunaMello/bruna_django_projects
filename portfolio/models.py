from django.db import models


# Create your models here.
class Project(models.Model):
    project_id = models.BigAutoField(primary_key=True)
    project_name = models.CharField(max_length=150)
    project_github = models.CharField(max_length=500)
    project_technology = models.CharField(max_length=150)
    project_description = models.TextField(blank=True)
    project_image = models.ImageField(blank=True)

    def __str__(self):
        return self.project_name





