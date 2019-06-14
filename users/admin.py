from django.contrib import admin
from .models import UserAccess 
from .models import Profile

# Register your models here.
admin.site.register(UserAccess)
admin.site.register(Profile)