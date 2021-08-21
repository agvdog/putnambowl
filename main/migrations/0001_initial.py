# Generated by Django 3.2.4 on 2021-08-19 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gamemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Carolina Panthers', 'Carolina Panthers'), ('Chicago Bears', 'Chicago Bears'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Detroit Lions', 'Detroit Lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New York Giants', 'New York Giants'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seattle Seahawks', 'Seattle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Washington', 'Washington'), ('Buffalo Bills', 'Buffalo Bills'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Denver Broncos', 'Denver Broncos'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Jacksonville Jaguars', 'Jacksonville Jaguars'), ('Miami Dolphins', 'Miami Dolphins'), ('New England Patriots', 'New England Patriots'), ('New York Jets', 'New York Jets'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('Tennessee Titans', 'Tennessee Titans')], default='Arizona Cardinals', max_length=20)),
                ('team2', models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Carolina Panthers', 'Carolina Panthers'), ('Chicago Bears', 'Chicago Bears'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Detroit Lions', 'Detroit Lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New York Giants', 'New York Giants'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seattle Seahawks', 'Seattle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Washington', 'Washington'), ('Buffalo Bills', 'Buffalo Bills'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Denver Broncos', 'Denver Broncos'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Jacksonville Jaguars', 'Jacksonville Jaguars'), ('Miami Dolphins', 'Miami Dolphins'), ('New England Patriots', 'New England Patriots'), ('New York Jets', 'New York Jets'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('Tennessee Titans', 'Tennessee Titans')], default='Arizona Cardinals', max_length=20)),
                ('points', models.FloatField(default=0)),
                ('winner', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.BooleanField(default=False)),
                ('week', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(max_length=10000, null=True)),
                ('week', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picks', models.TextField(max_length=200, null=True)),
                ('score', models.FloatField(default=0)),
                ('big_loser', models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Carolina Panthers', 'Carolina Panthers'), ('Chicago Bears', 'Chicago Bears'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Detroit Lions', 'Detroit Lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New York Giants', 'New York Giants'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seattle Seahawks', 'Seattle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Washington', 'Washington'), ('Buffalo Bills', 'Buffalo Bills'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Denver Broncos', 'Denver Broncos'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Jacksonville Jaguars', 'Jacksonville Jaguars'), ('Miami Dolphins', 'Miami Dolphins'), ('New England Patriots', 'New England Patriots'), ('New York Jets', 'New York Jets'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('Tennessee Titans', 'Tennessee Titans')], default='Arizona Cardinals', max_length=20)),
                ('nfc_champ', models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Carolina Panthers', 'Carolina Panthers'), ('Chicago Bears', 'Chicago Bears'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Detroit Lions', 'Detroit Lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New York Giants', 'New York Giants'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seattle Seahawks', 'Seattle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Washington', 'Washington')], default='Arizona Cardinals', max_length=20)),
                ('afc_champ', models.CharField(choices=[('Buffalo Bills', 'Buffalo Bills'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Denver Broncos', 'Denver Broncos'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Jacksonville Jaguars', 'Jacksonville Jaguars'), ('Miami Dolphins', 'Miami Dolphins'), ('New England Patriots', 'New England Patriots'), ('New York Jets', 'New York Jets'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('Tennessee Titans', 'Tennessee Titans')], default='Buffalo Bills', max_length=20)),
                ('superbowl_winner', models.CharField(choices=[('Arizona Cardinals', 'Arizona Cardinals'), ('Atlanta Falcons', 'Atlanta Falcons'), ('Carolina Panthers', 'Carolina Panthers'), ('Chicago Bears', 'Chicago Bears'), ('Dallas Cowboys', 'Dallas Cowboys'), ('Detroit Lions', 'Detroit Lions'), ('Green Bay Packers', 'Green Bay Packers'), ('Los Angeles Rams', 'Los Angeles Rams'), ('Minnesota Vikings', 'Minnesota Vikings'), ('New Orleans Saints', 'New Orleans Saints'), ('New York Giants', 'New York Giants'), ('Philadelphia Eagles', 'Philadelphia Eagles'), ('San Francisco 49ers', 'San Francisco 49ers'), ('Seattle Seahawks', 'Seattle Seahawks'), ('Tampa Bay Buccaneers', 'Tampa Bay Buccaneers'), ('Washington', 'Washington'), ('Buffalo Bills', 'Buffalo Bills'), ('Baltimore Ravens', 'Baltimore Ravens'), ('Cincinnati Bengals', 'Cincinnati Bengals'), ('Cleveland Browns', 'Cleveland Browns'), ('Denver Broncos', 'Denver Broncos'), ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'), ('Kansas City Chiefs', 'Kansas City Chiefs'), ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers', 'Los Angeles Chargers'), ('Jacksonville Jaguars', 'Jacksonville Jaguars'), ('Miami Dolphins', 'Miami Dolphins'), ('New England Patriots', 'New England Patriots'), ('New York Jets', 'New York Jets'), ('Pittsburgh Steelers', 'Pittsburgh Steelers'), ('Tennessee Titans', 'Tennessee Titans')], default='Arizona Cardinals', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]