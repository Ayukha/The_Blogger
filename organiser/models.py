from django.db import models

# Create your models here.
class Tag(models.Model):
	name=models.CharField(max_length=31, unique=True)
	slug=models.SlugField(max_length=31,unique=True,help_text='A label for URL config')


class Startup(models.Model):
	name=models.CharField(max_length=31,db_index=True)
	slug=max_length.SlugField(max_length=31,unique=True,help_text='A label for URL config.')
	description=models.TextField()
	founded_date=models.DateField('date founded')
	contact=models.EmailField()
	website=models.URLField(max_length=255)
	tags=models.ManyTOManyField(Tag)


class Newslink(models.Model):
	title=models.CharField(max_length=63)
	pub_date=models.DateField('date published')
	link=models.URLField(max_length=255)
	Startup=models.ForeignKey(Startup)



