# Generated by Django 4.1.3 on 2022-11-21 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0031_remove_submission_participant_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='answer',
        ),
        migrations.CreateModel(
            name='datoimp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.choice')),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.submission')),
            ],
        ),
    ]
