# Generated by Django 3.1.2 on 2020-11-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_post_imglink'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]