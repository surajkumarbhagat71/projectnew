# Generated by Django 2.2.7 on 2021-02-12 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('url_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('ed_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('datetime', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Url')),
            ],
        ),
    ]
