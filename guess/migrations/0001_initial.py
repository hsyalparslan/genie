# Generated by Django 2.1.3 on 2018-12-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_number', models.CharField(default='DEFAULT', max_length=100)),
                ('c_1', models.CharField(default='DEFAULT', max_length=10000)),
                ('c_2', models.CharField(default='DEFAULT', max_length=10000)),
                ('c_3', models.CharField(default='DEFAULT', max_length=10000)),
                ('c_4', models.CharField(default='DEFAULT', max_length=10000)),
                ('c_5', models.CharField(default='DEFAULT', max_length=10000)),
                ('c_6', models.CharField(default='DEFAULT', max_length=10000)),
            ],
        ),
    ]
