# Generated by Django 4.1.5 on 2023-01-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]