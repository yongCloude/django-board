from logging import getLogger
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from auths.models import Profile

# Create your models here.

class Post(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, blank = True)
    title = models.CharField(max_length = 128)
    category = models.CharField(max_length = 128)
    body = models.TextField()
    image = models.ImageField(upload_to = 'post/', default = 'default.png')
    published_date = models.DateTimeField(default = timezone.now)


class  Like(models.Model) :
    Post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)