# Generated by Django 2.2.3 on 2019-07-11 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('serviceid', models.IntegerField(primary_key=True, serialize=False)),
                ('servicename', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('cancelfee', models.IntegerField()),
                ('refund', models.IntegerField()),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
