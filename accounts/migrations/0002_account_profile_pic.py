# Generated by Django 3.2.9 on 2021-11-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='photos/users/pofile_pics'),
        ),
    ]
