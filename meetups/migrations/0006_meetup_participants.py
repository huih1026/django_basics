# Generated by Django 3.2.7 on 2021-09-05 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, to='meetups.Participant'),
        ),
    ]
