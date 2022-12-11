from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length = 5000)
    #image = models.ImageField(upload_to='img/portfolio/')
    description = models.TextField(max_length=5000)
    tags = models.CharField(max_length=100, null= True)
    github_url = models.URLField(max_length = 1000)


    class Meta:
        db_table="project"

class Visitor(models.Model):
    ip = models.CharField(max_length=500)
    visit_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="visitor"
