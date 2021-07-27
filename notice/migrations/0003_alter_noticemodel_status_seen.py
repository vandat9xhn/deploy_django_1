# Generated by Django 3.2.3 on 2021-07-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_alter_noticemodel_link_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticemodel',
            name='status_seen',
            field=models.IntegerField(choices=[(0, 'sent'), (1, 'received'), (2, 'seen')]),
        ),
    ]
