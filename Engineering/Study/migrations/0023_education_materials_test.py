# Generated by Django 4.2.1 on 2024-05-21 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0022_remove_studytest_question_studytest_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='education_materials',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Study.studytest'),
        ),
    ]
