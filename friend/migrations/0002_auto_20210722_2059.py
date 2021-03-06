# Generated by Django 3.2.3 on 2021-07-22 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_personalsettingmodel_permission_see_interactive'),
        ('friend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendmodel',
            old_name='receiver',
            new_name='friend_model',
        ),
        migrations.RenameField(
            model_name='friendmodel',
            old_name='requester',
            new_name='profile_model',
        ),
        migrations.AddField(
            model_name='friendmodel',
            name='is_follow',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='friendmodel',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='addfriendmodel',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='friendmodel',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='FriendRemoveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_fr_rm_pf_f', to='user_profile.profilemodel')),
                ('profile_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_fr_rm_pf', to='user_profile.profilemodel')),
            ],
        ),
    ]
