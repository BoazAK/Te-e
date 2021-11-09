# Generated by Django 3.2.9 on 2021-11-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_points', '0005_point_point_disponibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='image1',
            field=models.ImageField(default='None', upload_to='food_point_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='point',
            name='image2',
            field=models.ImageField(default='None', upload_to='food_point_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='point',
            name='point_disponibility',
            field=models.BooleanField(default=True),
        ),
    ]
