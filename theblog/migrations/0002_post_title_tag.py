# Generated by Django 4.1.4 on 2022-12-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Its a nice blog post title', max_length=120),
        ),
    ]