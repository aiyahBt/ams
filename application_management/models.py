from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now
# Create your models here.

class ApplicationRound(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length=100, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    visible = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.title, self.start_date, self.active)


# Function for ImageUploadingTest
def user_image_directory(instance, filename):
    date = datetime.datetime.now().date()
    date = date.__str__().replace('-', '/')

    return 'application_management/user_{0}/images/{1}/{2}'.format(instance.user.id, date, filename)

def user_document_directory(instance, filename):
    date = datetime.datetime.now().date()
    date = date.__str__().replace('-', '/')
    return 'application_management/user_{0}/doc/{1}/{2}'.format(instance.user.id, date, filename)

class ApplicationFormModel(models.Model):

    application_round = models.ForeignKey(ApplicationRound, null=True,  on_delete=models.CASCADE)
    user  = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    prefix = models.CharField(max_length=20, null=True)
    firstname  = models.CharField(max_length=40, null=True, )
    middlename = models.CharField(max_length=40, null=True, blank=True)
    lastname = models.CharField(max_length=40, null=True)
    birthdate = models.DateField(null=True)
    email = models.EmailField(null=True)
    phonenumber = models.IntegerField(null=True)
    gpax = models.FloatField(null=True)

    student_image = models.ImageField(null=True)
    transcript = models.FileField(null=True)
    optional_work = models.FileField(null=True, blank=True)

    # title = models.CharField(max_length=200)
    # image = models.ImageField(upload_to=user_image_directory, null=True)
    # doc   = models.FileField(upload_to=user_document_directory, null=True)


    def __str__(self):
        return '{} {}'.format(self.application_round.title, self.user.username)

