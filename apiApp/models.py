from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from allauth.socialaccount.models import SocialAccount
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.sqlite.fields import ArrayField

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,blank=False,verbose_name = "First Name")
    last_name = models.CharField(max_length=200, blank=False,verbose_name = "Last Name")

    # profile_pic = models.ImageField(upload_to='profile_pics',verbose_name="Profile Picture")

    # day = models.CharField(max_length=5,blank=True)
    # month = models.CharField(max_length=5,blank=True)
    # year = models.CharField(max_length=5,blank=True)

    gender = models.CharField(max_length=10,blank=True)

    # city = models.CharField(max_length=20,blank=True)
    country = models.CharField(max_length=20,blank=True)

    # about = models.CharField(max_length=2000,blank=True)

    class Meta:
        verbose_name = "User Profile"

    def __str__(self):
        return self.user.username

# class customUser(models.Model):
# 	sex = models.IntegerField(blank=False,unique=True)
# 	def setAttr(self, obj):
# 		print(obj.user.id)
	


class genre(models.Model):
	genre_id=models.IntegerField(blank=False,unique=True)
	genre_name=models.CharField(max_length=500)

	def __str__(self):
		return self.genre_name
