# Generated by Django 4.2.1 on 2024-04-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0002_filesforex_remove_education_materials_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filesforex',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
