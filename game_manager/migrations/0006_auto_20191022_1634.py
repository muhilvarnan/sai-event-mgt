# Generated by Django 2.2.6 on 2019-10-22 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_manager', '0005_eventmark_eventparticipant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventparticipant',
            name='participant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game_manager.Participant'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game_manager.Team'),
        ),
    ]
