# Generated by Django 2.1.7 on 2019-04-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0029_auto_20190407_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_id',
            field=models.CharField(default='12345', max_length=20, verbose_name='Номер договора'),
            preserve_default=False,
        ),
    ]
