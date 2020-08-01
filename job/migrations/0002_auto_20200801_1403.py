# Generated by Django 3.0.8 on 2020-08-01 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=' ', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]
