# Generated by Django 2.1.7 on 2019-04-06 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0015_auto_20190406_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='offers',
        ),
        migrations.RemoveField(
            model_name='ratingandreview',
            name='item',
        ),
        migrations.AddField(
            model_name='offer',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Item', verbose_name='Работа'),
        ),
    ]
