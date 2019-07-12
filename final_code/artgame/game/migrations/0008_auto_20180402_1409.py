# Generated by Django 2.0.2 on 2018-04-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20180328_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='games_played',
            field=models.PositiveIntegerField(default=0, verbose_name='Games Played'),
        ),
        migrations.AddField(
            model_name='player',
            name='high_score',
            field=models.PositiveIntegerField(default=0, verbose_name='High Score'),
        ),
        migrations.AddField(
            model_name='player',
            name='total_score',
            field=models.PositiveIntegerField(default=0, verbose_name='Total Score'),
        ),
    ]