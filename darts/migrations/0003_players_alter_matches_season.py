# Generated by Django 5.1.4 on 2024-12-23 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darts', '0002_alter_seasons_options_matches'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.AlterField(
            model_name='matches',
            name='season',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='match', to='darts.seasons'),
        ),
    ]
