from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#we will be updating the user model to have a one to one relation with the profile

class UserAccess(models.Model):
    access_level = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=150)
    class Meta:
        verbose_name = "UserAccess"
        verbose_name_plural = "UserAccess"
        db_table = 'UserAccess'

    def __str__(self):
        return f'{self.access_level}  {self.description}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    user_access = models.ForeignKey(UserAccess, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        db_table = 'Profile'

    def __str__(self):
        return f'{self.user.username} Profile'      