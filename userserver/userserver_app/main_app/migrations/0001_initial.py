# Generated by Django 4.0.1 on 2022-01-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(choices=[(0, 'Afryka'), (1, 'Ameryka Południowa'), (2, 'Ameryka Północna'), (3, 'Antarktyda'), (4, 'Australia'), (5, 'Azja'), (6, 'Europa')], default=0, verbose_name='Głos')),
            ],
        ),
    ]
