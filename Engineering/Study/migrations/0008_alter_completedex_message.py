# Generated by Django 4.2.1 on 2024-04-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0007_completedex_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedex',
            name='message',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
