# Generated by Django 4.0.6 on 2022-08-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_postjob'),
    ]

    operations = [
        migrations.CreateModel(
            name='applyjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('exper', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('iname', models.FileField(upload_to='jobapp/static')),
            ],
        ),
    ]
