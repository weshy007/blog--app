from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset()\
                .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                                related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, 
                                choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() #Our default manager
    published = PublishManager() # Our custom manager
    

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

'''
There are two ways to add or customize managers for your models: you can
add extra manager methods to an existing manager, or create a new manager by
modifying the initial QuerySet that the manager returns. The first method provides
you with a QuerySet API such as Post.objects.my_manager(), and the latter provides you with Post.my_manager.all(). 
The manager will allow you to retrieve posts using Post.published.all().
'''

    

