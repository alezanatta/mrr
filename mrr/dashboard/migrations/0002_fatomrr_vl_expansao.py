# Generated by Django 3.0.7 on 2020-11-12 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fatomrr',
            name='vl_expansao',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
