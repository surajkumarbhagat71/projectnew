# Generated by Django 2.2.7 on 2021-02-13 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventdetail',
            name='description',
        ),
        migrations.RemoveField(
            model_name='eventdetail',
            name='image',
        ),
        migrations.AlterField(
            model_name='eventdetail',
            name='datetime',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='eventdetail',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='eventdetail',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
