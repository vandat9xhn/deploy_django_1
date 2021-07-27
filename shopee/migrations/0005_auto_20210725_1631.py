# Generated by Django 3.2.3 on 2021-07-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopee', '0004_auto_20210612_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vouchermodel',
            old_name='condition_price',
            new_name='min_amount',
        ),
        migrations.AddField(
            model_name='vouchermodel',
            name='count_user',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vouchermodel',
            name='expires',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vouchermodel',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='vouchermodel',
            name='info',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='vouchermodel',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vouchermodel',
            name='total_num',
            field=models.IntegerField(default=100),
        ),
    ]
