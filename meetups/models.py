from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}({self.address})'


class Participant(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.firstname} is here'


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True)

    def __str__(self):
        return f'{self.title}'

    # def get_absolute_url(self):
    #     return reverse("meetup-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
