# Generated by Django 5.1.4 on 2024-12-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0004_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_images/default.jpg', null=True, upload_to='profile_images/'),
        ),
    ]
