# Generated by Django 4.2.1 on 2024-05-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0025_completedex_count_quests'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedex',
            name='finish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='completedex',
            name='start',
            field=models.BooleanField(default=False),
        ),
    ]
