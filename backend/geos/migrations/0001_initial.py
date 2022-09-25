# Generated by Django 4.1.1 on 2022-09-24 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longtitude', models.FloatField()),
                ('altitude', models.FloatField()),
                ('identifier', models.CharField(blank=True, max_length=150, null=True)),
                ('timestamp', models.IntegerField()),
                ('floor_label', models.IntegerField(blank=True, null=True)),
                ('horizontal_accuracy', models.FloatField()),
                ('vertical_accuracy', models.FloatField()),
                ('confidence', models.FloatField(default=0.6827)),
                ('activity', models.CharField(max_length=100)),
                ('slide', models.IntegerField()),
            ],
        ),
    ]
