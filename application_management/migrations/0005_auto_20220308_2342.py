# Generated by Django 3.2.5 on 2022-03-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_management', '0004_rename_imageuploadingtest_applicationformmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationformmodel',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='applicationformmodel',
            name='image',
        ),
        migrations.RemoveField(
            model_name='applicationformmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='firstname',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='gpax',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='lastname',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='middlename',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='optional_work',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='phonenumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='prefix',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='student_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='transcript',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
