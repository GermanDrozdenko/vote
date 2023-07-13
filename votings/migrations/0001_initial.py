# Generated by Django 4.2.3 on 2023-07-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                )),
                ('title', models.CharField(max_length=60)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('max_votes', models.IntegerField(blank=True, null=True)),
                ('expired', models.BooleanField(default=False)),
                ('first_char_votes', models.IntegerField(default=0)),
                ('second_char_votes', models.IntegerField(default=0)),
                ('characters', models.ManyToManyField(
                    related_name='characters', to='characters.character'
                )),
            ],
        ),
    ]
