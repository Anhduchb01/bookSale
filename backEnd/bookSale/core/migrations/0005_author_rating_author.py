# Generated by Django 4.1.4 on 2022-12-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.IntegerField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'author',
                'ordering': ['author_id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rating_Author',
            fields=[
                ('rating_id', models.IntegerField(primary_key=True, serialize=False)),
                ('author_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('rating', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rating',
                'managed': False,
            },
        ),
    ]
