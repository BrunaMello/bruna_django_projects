# Generated by Django 4.1 on 2022-11-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0004_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=150)),
                ('project_github', models.CharField(max_length=500)),
                ('project_technology', models.CharField(max_length=150)),
                ('project_description', models.TextField(blank=True)),
                ('project_image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
