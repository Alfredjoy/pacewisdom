# Generated by Django 3.1.4 on 2020-12-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
