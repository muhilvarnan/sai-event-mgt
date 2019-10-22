# Generated by Django 2.2.6 on 2019-10-22 16:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('game_manager', '0004_event_eventcriteria'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_manager.Event')),
                ('participant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game_manager.Participant')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game_manager.Team')),
            ],
        ),
        migrations.CreateModel(
            name='EventMark',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('judge_name', models.CharField(max_length=255)),
                ('mark', models.IntegerField()),
                ('event_criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_manager.EventCriteria')),
                ('event_participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_manager.EventParticipant')),
            ],
        ),
    ]
