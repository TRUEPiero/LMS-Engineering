# Generated by Django 4.2.1 on 2024-04-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education_materials',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
