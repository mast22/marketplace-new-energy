# Generated by Django 2.1.7 on 2019-04-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_item_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='oriented_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Ориентировочная цена работ'),
        ),
    ]
