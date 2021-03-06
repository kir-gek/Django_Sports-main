# Generated by Django 4.0.4 on 2022-06-07 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название матча')),
                ('score1', models.IntegerField(default=0, verbose_name='Счёт команды 1')),
                ('score2', models.IntegerField(default=0, verbose_name='Счёт команды 2')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название команды')),
                ('type_of_sport', models.CharField(default='', max_length=50, verbose_name='Вид спорта')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название турнира')),
                ('description', models.TextField(verbose_name='Описание турнира')),
                ('status', models.CharField(choices=[('PLANNED', 'Планируется'), ('LIVE', 'В процессе'), ('FINISHED', 'Завершён')], default='PLANNED', max_length=255, verbose_name='Статус турнира')),
                ('games', models.ManyToManyField(related_name='Tournament', to='sports.game', verbose_name='Игры')),
                ('teams', models.ManyToManyField(related_name='Tournament', to='sports.team', verbose_name='Команды')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.team', verbose_name='Победитель турнира')),
            ],
            options={
                'verbose_name': 'Турнир',
                'verbose_name_plural': 'Турниры',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='sports.team', verbose_name='Команда 1'),
        ),
        migrations.AddField(
            model_name='game',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='sports.team', verbose_name='Команда 2'),
        ),
    ]
