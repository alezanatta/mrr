# Generated by Django 3.0.7 on 2020-11-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_fatomrr_vl_expansao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controleversao',
            name='cd_versao',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dimano',
            name='cd_ano',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dimcliente',
            name='cd_cliente',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dimdia',
            name='cd_dia',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dimlocalidade',
            name='cd_localidade',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dimmes',
            name='cd_mes',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dimplano',
            name='cd_plano',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dimsegmento',
            name='cd_segmento',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fatomrr',
            name='cd_fato_mrr',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
