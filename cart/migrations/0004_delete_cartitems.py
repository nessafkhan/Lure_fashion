# Generated by Django 3.2.9 on 2021-11-19 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cartitems'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItems',
        ),
    ]