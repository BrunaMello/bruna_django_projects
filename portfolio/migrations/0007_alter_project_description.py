# Generated by Django 4.1 on 2022-11-02 10:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_project_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]