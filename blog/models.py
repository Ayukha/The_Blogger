from django.db import models
from organiser.models import Startup,Tag

# Create your models here.
class Post(models.Model):

	title=models.CharField(max_length=63)
	slug=models.slugField()
	text=models.TextField()
	pub_date=models.DateField()
	tags = models.ManyToManyField(Tag)
    startups = models.ManyToManyField(Startup)