# Generated by Django 3.0 on 2022-06-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('roll', models.IntegerField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
