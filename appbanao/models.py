from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone

user_role = (
    ('Patient', 'Patient'),
    ('Doctor', 'Doctor'),
    )


class CustomManager(models.Manager):    
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=8, choices=user_role, default='Role')
    profile_photo = models.ImageField(upload_to='images/profile_photo', blank=True, null=True, default="profile_photo/avatar.svg")
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    CATEGORY_CHOICES = (('Mental Health', 'Mental Health'), ('Heart Disease', 'Heart Disease'), ('Covid19', 'Covid19'), ('Immunization', 'Immunization'))
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=264, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Category')
    body = models.TextField()
    photos = models.ImageField(upload_to='images/blog_photos', blank=True, null=True, default="user-group.svg")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = CustomManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])
