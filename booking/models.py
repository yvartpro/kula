from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
      email =  models.EmailField(unique=True)
      phone = models.IntegerField(null=True)
      address = models.CharField(max_length=30,null=True)
      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = []
      def __str__(self):
          return self.email

class Booking(models.Model):
      company = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      full_name = models.CharField(max_length=20)
      email = models.EmailField()
      people = models.IntegerField() 
      time = models.TimeField()
      date = models.DateField()
      type = models.CharField(max_length=20)
      special_request = models.TextField()
      vovotapesa = models.IntegerField()
      phone  = models.IntegerField(null=True)
      def __str__(self):
          return self.full_name

class Post(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      photo = models.FileField(upload_to='post/')
      title = models.CharField(max_length=20)
      description = models.CharField(max_length=255)
      def __str__(self):
          return f'self.user.first_name'
class Profile(models.Model):
      user = models.OneToOneField(User,on_delete=models.CASCADE)
      photo = models.FileField(upload_to='profile/')
      def __str__(self):
          return f'{self.user.email}'

          return f'{self.user.email}'
class Category(models.Model):
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
      category = models.CharField(max_length=30)
      def __str__(self):
          return f'{self.user.email}'
