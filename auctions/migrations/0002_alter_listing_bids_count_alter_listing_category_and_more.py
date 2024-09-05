# Generated by Django 4.2.2 on 2023-07-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bids_count',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('ARTS', 'Art & Collectibles'), ('FOOD', 'Food & Beverages'), ('DYI', 'DYI'), ('GAME', 'Games & entertainment'), ('HOME', 'Home'), ('CLOTH', 'Clothing'), ('MISC', 'Miscellaneous')], max_length=30),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
