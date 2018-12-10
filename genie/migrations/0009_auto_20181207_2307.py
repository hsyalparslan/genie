# Generated by Django 2.1.3 on 2018-12-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genie', '0008_tasktwogenie_wishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_total', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='tasktwocustomer',
            name='c_wish',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tasktwogenie',
            name='g_choice',
            field=models.CharField(default='DEFAULT', max_length=10000),
        ),
        migrations.AlterField(
            model_name='tasktwogenie',
            name='g_name',
            field=models.CharField(default='DEFAULT', max_length=100),
        ),
        migrations.AlterField(
            model_name='tasktwogenie',
            name='wishes',
            field=models.CharField(default='DEFAULT', max_length=1000),
        ),
    ]
