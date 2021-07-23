# Generated by Django 3.1.7 on 2021-07-23 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('packed', 'Packed'), ('on the way', 'On The Way'), ('delivered', 'Delivered'), ('cancel', 'Cancel')], default='Pending', max_length=50),
        ),
    ]
