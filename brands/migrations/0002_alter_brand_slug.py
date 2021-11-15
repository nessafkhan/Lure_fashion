# Generated by Django 3.2.9 on 2021-11-14 12:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, max_length=100, unique=True),
        ),
    ]