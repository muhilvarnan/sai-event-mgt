# Generated by Django 2.2.6 on 2019-10-28 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_manager', '0019_auto_20191028_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='group',
        ),
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.ManyToManyField(blank=True, help_text='Groups in which paritcipants may in for the event', to='game_manager.Group', verbose_name='Participant falling group'),
        ),
    ]
