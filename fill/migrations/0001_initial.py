# Generated by Django 2.1.3 on 2018-12-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_number', models.CharField(default='DEFAULT', max_length=100)),
                ('f_1', models.CharField(default='DEFAULT', max_length=10000)),
                ('f_2', models.CharField(default='DEFAULT', max_length=10000)),
                ('f_3', models.CharField(default='DEFAULT', max_length=10000)),
                ('f_4', models.CharField(default='DEFAULT', max_length=10000)),
                ('f_5', models.CharField(default='DEFAULT', max_length=10000)),
                ('f_6', models.CharField(default='DEFAULT', max_length=10000)),
                ('f_7', models.CharField(default='DEFAULT', max_length=10000)),
                ('f_8', models.CharField(default='DEFAULT', max_length=10000)),
            ],
        ),
    ]