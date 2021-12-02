# Generated by Django 3.2.9 on 2021-12-02 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20211201_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Order confirmed', 'Order confirmed'), ('Shipped', 'Shipped'), ('Out for Delivery', 'Out of Delivery'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='New', max_length=50),
        ),
    ]