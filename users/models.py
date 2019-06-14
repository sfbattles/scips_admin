from django.db import models
from django.contrib.auth.models import User
from PIL import Image
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

    #this super() function runs the parent class save.  Then we will grab the image that was upload
    #and scale it to be a smaller image.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  #this runs even if we didn't create our own save function we are adding addition fucntionality to it.

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)