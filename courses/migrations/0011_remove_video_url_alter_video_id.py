# Generated by Django 4.1.7 on 2023-03-31 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_rename_co_slug_course_slug_remove_course_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.CharField(max_length=2500, primary_key=True, serialize=False),
        ),
    ]
