# Generated by Django 2.2.6 on 2019-10-22 15:42

from django.db import migrations, models
import game_manager.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('game_manager', '0002_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(default=game_manager.models.random_string, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('participants', models.ManyToManyField(to='game_manager.Participant')),
            ],
        ),
    ]
