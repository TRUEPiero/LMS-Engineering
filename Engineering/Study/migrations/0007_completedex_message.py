# Generated by Django 4.2.1 on 2024-04-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0006_alter_completedex_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedex',
            name='message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
