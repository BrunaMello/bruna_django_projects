# Generated by Django 4.1 on 2022-11-02 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_project_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technology_name',
            field=models.CharField(choices=[(0, 'JavaScript'), (1, 'Java'), (2, 'Python'), (4, 'Android'), (5, 'Apple'), (6, 'Other')], default=6, max_length=10),
        ),
    ]