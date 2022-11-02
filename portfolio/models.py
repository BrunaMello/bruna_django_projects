from django.db import models
from django.utils.timezone import now
from tinymce.models import HTMLField

# Create your models here.

TECHNOLOGY = (
    (0, "JavaScript"),
    (1, "Java"),
    (2, "Python"),
    (3, "Android"),
    (4, "Apple"),
    (5, "Other")
)


class Project(models.Model):
    project_id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    github = models.CharField(max_length=500)
    technology = models.IntegerField(choices=TECHNOLOGY, default=6)
    summary = models.TextField(max_length=200)
    description = HTMLField()
    date_created = models.DateTimeField(default=now)
    project_image = models.ImageField(blank=True)

    class Meta:
        ordering = ['technology']

    def __str__(self):
        return self.title
