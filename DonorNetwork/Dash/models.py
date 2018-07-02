from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    #links UserProfile to User model instance
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    #additional attributes besides name, email, password, username
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
