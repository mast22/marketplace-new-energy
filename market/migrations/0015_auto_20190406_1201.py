# Generated by Django 2.1.7 on 2019-04-06 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0014_item_choosen'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingAndReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('review', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='choosen',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='choosen',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='item',
        ),
        migrations.AddField(
            model_name='ratingandreview',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Item'),
        ),
        migrations.AddField(
            model_name='ratingandreview',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Offer'),
        ),
        migrations.AddField(
            model_name='item',
            name='offers',
            field=models.ManyToManyField(through='market.RatingAndReview', to='market.Offer'),
        ),
    ]
