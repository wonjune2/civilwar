# Generated by Django 3.1.7 on 2021-05-23 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blue', models.CharField(max_length=5)),
                ('red', models.CharField(max_length=5)),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': '이미 존재하는 이름입니다.'}, max_length=20, unique=True)),
                ('total', models.PositiveIntegerField(default=0)),
                ('win', models.PositiveIntegerField(default=0)),
                ('lose', models.PositiveIntegerField(default=0)),
                ('winrate', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=5)),
                ('camp', models.CharField(max_length=10)),
                ('create_date', models.DateTimeField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lolteams.league')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lolteams.member')),
            ],
        ),
    ]
