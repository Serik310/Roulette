# Generated by Django 3.2.2 on 2021-05-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BetHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winning_number', models.IntegerField(verbose_name='Winning number')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
            ],
        ),
    ]
