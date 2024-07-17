# Generated by Django 5.0.6 on 2024-07-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_alter_listing_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
