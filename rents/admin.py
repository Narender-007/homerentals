from django.contrib import admin


# Register your models here.
from .models import RegistrationModel, CommentsModel,UploadrentsModel,BookingModel,RatingModel

admin.site.register(RegistrationModel)
admin.site.register(UploadrentsModel)
admin.site.register(BookingModel)
admin.site.register(RatingModel)
admin.site.register(CommentsModel)


