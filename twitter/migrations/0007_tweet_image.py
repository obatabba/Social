# Generated by Django 5.1.4 on 2024-12-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0006_tweet_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_images/'),
        ),
    ]
