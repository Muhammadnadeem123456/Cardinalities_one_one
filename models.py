from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class User(models.Model):
    # user_name=models.CharField(max_length=50)
    # password=models.CharField(max_length=50)


class Page(models.Model):
    #if we want to del post not his user for seek of that we will use models.protect
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    #if we want del user not his/her post for seek of that we will do models.set_null,null=true
    # user=models.OneToOneField(User,on_delete=models.PROTECT)
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    pag_name=models.CharField(max_length=50)
    pag_cat=models.CharField()
    pag_publish_date=models.DateField()

