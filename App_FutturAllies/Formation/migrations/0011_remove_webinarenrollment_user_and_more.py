# Generated by Django 4.2 on 2024-11-21 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Formation', '0010_remove_webinar_enddatetime_remove_webinar_speaker_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webinarenrollment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='webinarenrollment',
            name='webinarId',
        ),
        migrations.DeleteModel(
            name='Webinar',
        ),
        migrations.DeleteModel(
            name='WebinarEnrollment',
        ),
    ]
