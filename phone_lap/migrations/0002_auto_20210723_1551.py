# Generated by Django 3.2.3 on 2021-07-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_lap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonelapmodel',
            name='camera_type',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='phonelapmodel',
            name='internal_memory_lv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='phonelapmodel',
            name='memory_stick_lv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='phonelapmodel',
            name='ram_lv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='phonelapmodel',
            name='special',
            field=models.CharField(default='', max_length=500),
        ),
    ]
