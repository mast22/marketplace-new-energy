# Generated by Django 2.1.7 on 2019-04-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_item_extra_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='Сделать что то', max_length=100, verbose_name='Краткое описание работ'),
            preserve_default=False,
        ),
    ]
