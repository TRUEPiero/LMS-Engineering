# Generated by Django 4.2.1 on 2024-05-21 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0020_grades_date_created_grades_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=255, null=True)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionForTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, max_length=255, null=True)),
                ('choise', models.ManyToManyField(blank=True, to='Study.choise')),
            ],
        ),
        migrations.CreateModel(
            name='StudyTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Study.questionfortest')),
            ],
        ),
    ]
