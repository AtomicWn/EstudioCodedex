# Generated by Django 4.1.3 on 2022-11-21 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0032_remove_submission_answer_datoimp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datoimp',
            old_name='answer',
            new_name='ans',
        ),
        migrations.AddField(
            model_name='submission',
            name='answer',
            field=models.ManyToManyField(to='Home.choice'),
        ),
    ]
