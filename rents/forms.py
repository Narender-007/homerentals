from django.forms import Form,CharField,EmailField,PasswordInput,FileField
from django.forms import Form, ImageField, CharField

# Create your models here.
class RegistrationForm(Form):
    fname = CharField(max_length=20)
    lname = CharField(max_length=30)
    pathh = FileField()
    age = CharField(max_length=20)
    username = CharField(max_length=10)
    password = CharField(max_length=12)
    gender = CharField(max_length=20)
    phone = CharField(max_length=10)
    mail = EmailField(max_length=26)
    addres = CharField(max_length=60)
    occupation = CharField(max_length=40)
    workingarea = CharField(max_length=40)
    company = CharField(max_length=60)

class LoginForm(Form):
    username = CharField(max_length=20)
    password = CharField(widget=PasswordInput())
    


class UploadrentsForm(Form):
    name = CharField(max_length=100)
    image = FileField()
    price = CharField(max_length=100)
    location = CharField(max_length=100)
    description = CharField(max_length=100)
    housetype = CharField(max_length=100)


class CommentsForm(Form):
    text = CharField(max_length=100)
    product = CharField(max_length=100)
    datetime = CharField(max_length=10)
    user = CharField(max_length=100)

class BookingForm(Form):
    name = CharField(max_length=100)
    cardno = CharField(max_length=100)
    cvvno = CharField(max_length=3)
    phone = CharField(max_length=10)
    email = CharField(max_length=100)

class RatingForm(Form):
    rating = CharField(max_length=100)

    
class UploadForm(Form):
    name = CharField(max_length=100)
    price = CharField(max_length=100)
    location = CharField(max_length=100)
    housetype = CharField(max_length=100)
    myfile=ImageField()
    description=CharField(max_length=400)