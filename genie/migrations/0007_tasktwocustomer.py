# Generated by Django 2.1.3 on 2018-12-04 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genie', '0006_auto_20181204_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskTwoCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
                ('c_wish', models.CharField(max_length=50)),
            ],
        ),
    ]