# Generated by Django 2.1.3 on 2018-12-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_number', models.CharField(default='DEFAULT', max_length=100)),
                ('q_1', models.CharField(default='DEFAULT', max_length=10000)),
                ('q_2', models.CharField(default='DEFAULT', max_length=10000)),
                ('q_3', models.CharField(default='DEFAULT', max_length=10000)),
                ('q_4', models.CharField(default='DEFAULT', max_length=10000)),
                ('q_5', models.CharField(default='DEFAULT', max_length=10000)),
                ('q_6', models.CharField(default='DEFAULT', max_length=10000)),
                ('q_7', models.CharField(default='DEFAULT', max_length=10000)),
                ('q_8', models.CharField(default='DEFAULT', max_length=10000)),
                ('q_9', models.CharField(default='DEFAULT', max_length=10000)),
            ],
        ),
    ]
