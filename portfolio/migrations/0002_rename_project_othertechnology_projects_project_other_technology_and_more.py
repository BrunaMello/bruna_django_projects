# Generated by Django 4.1 on 2022-11-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='project_othertechnology',
            new_name='project_other_technology',
        ),
        migrations.AddField(
            model_name='projects',
            name='project_github',
            field=models.CharField(default='url', max_length=500),
        ),
    ]
