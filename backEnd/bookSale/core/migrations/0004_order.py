# Generated by Django 4.1.4 on 2022-12-17 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_shoppingcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('product_num', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('order_time', models.TimeField()),
            ],
            options={
                'db_table': 'order',
                'ordering': ['order_id'],
                'managed': False,
            },
        ),
    ]
