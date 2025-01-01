# Generated by Django 5.1.4 on 2024-12-23 17:25

import darts.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darts', '0003_players_alter_matches_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='season',
            field=models.ForeignKey(default=darts.models.get_last_season_id, on_delete=django.db.models.deletion.CASCADE, to='darts.seasons'),
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveSmallIntegerField()),
                ('darts', models.PositiveSmallIntegerField()),
                ('result', models.CharField(choices=[('W', 'Won'), ('L', 'Lost'), ('S', 'Set')], max_length=1)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darts.matches')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darts.players')),
            ],
            options={
                'verbose_name_plural': 'Games',
            },
        ),
    ]