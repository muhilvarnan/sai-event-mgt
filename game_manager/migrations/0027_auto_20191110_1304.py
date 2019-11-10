# Generated by Django 2.2.6 on 2019-11-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_manager', '0026_participantfamily_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='arrival_point',
            field=models.CharField(choices=[('Direct to Mandapam', 'Direct to Mandapam'), ('Railway Station', 'Railway Station'), ('Old Bus Stand', 'Old Bus Stand'), ('New Bus Stand', 'New Bus Stand')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='participant',
            name='departure_point',
            field=models.CharField(choices=[('Direct to Mandapam', 'Direct to Mandapam'), ('Railway Station', 'Railway Station'), ('Old Bus Stand', 'Old Bus Stand'), ('New Bus Stand', 'New Bus Stand')], default=None, max_length=50),
        ),
    ]
