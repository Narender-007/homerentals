from django.db import models

# Create your models here.
class RegistrationModel(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=30)
    age = models.CharField(max_length=20)
    pathh = models.FileField(upload_to="pictures")
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=12)
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    mail = models.EmailField(max_length=26)
    addres = models.CharField(max_length=60)
    occupation = models.CharField(max_length=40)
    workingarea = models.CharField(max_length=40)
    company = models.CharField(max_length=60)
    def __str__(self):
        return self.lname

class CommentModel(models.Model):

    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.CharField(max_length=60)
    product = models.CharField(max_length=60)


class UploadrentsModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pictures")
    price = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    housetype = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CommentsModel(models.Model):
    text = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now=True, blank=True)
    user = models.CharField(max_length=100)

class BookingModel(models.Model):
    name = models.CharField(max_length=100)
    cardno = models.CharField(max_length=100)
    cvvno = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)

class RatingModel(models.Model):

    rating = models.CharField(max_length=100,default="0")
    user = models.CharField(max_length=60)
    product = models.CharField(max_length=60)



class ImageModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    housetype = models.CharField(max_length=100)
    myfile=models.ImageField(upload_to="pictures")
    class Meta:
        db_table="myfiles"