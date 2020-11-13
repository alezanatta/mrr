# Generated by Django 3.0.7 on 2020-11-11 17:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControleVersao',
            fields=[
                ('cd_versao', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('dt_versao', models.DateField(default=datetime.date.today)),
                ('fato_versao', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='DimAno',
            fields=[
                ('cd_ano', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DimCliente',
            fields=[
                ('cd_cliente', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nr_cliente', models.IntegerField()),
                ('nm_cliente', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('nr_cliente', 'nm_cliente')},
            },
        ),
        migrations.CreateModel(
            name='DimDia',
            fields=[
                ('cd_dia', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('dia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DimLocalidade',
            fields=[
                ('cd_localidade', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nm_cidade', models.CharField(max_length=75)),
                ('nm_estado', models.CharField(max_length=75)),
            ],
            options={
                'unique_together': {('nm_cidade', 'nm_estado')},
            },
        ),
        migrations.CreateModel(
            name='DimMes',
            fields=[
                ('cd_mes', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nr_mes', models.IntegerField()),
                ('nm_mes', models.CharField(max_length=10, unique=True)),
                ('sg_mes', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DimPlano',
            fields=[
                ('cd_plano', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nm_plano', models.CharField(max_length=75, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DimSegmento',
            fields=[
                ('cd_segmento', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nm_segmento', models.CharField(max_length=75, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FatoSegmento',
            fields=[
                ('cd_fato_segmento', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('vl_mrr', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('vl_cancelamento', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cd_ano', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimAno')),
                ('cd_localidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimLocalidade')),
                ('cd_mes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimMes')),
                ('cd_plano', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimPlano')),
                ('cd_segmento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimSegmento')),
            ],
        ),
        migrations.CreateModel(
            name='FatoMrr',
            fields=[
                ('cd_fato_mrr', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('periodicidade', models.IntegerField(default=1)),
                ('vl_mrr', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('vl_cancelamento', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('sn_novo', models.BooleanField(default=False)),
                ('sn_cancelado', models.BooleanField(default=False)),
                ('sn_renascido', models.BooleanField(default=False)),
                ('cd_ano', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimAno')),
                ('cd_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimCliente')),
                ('cd_dia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimDia')),
                ('cd_localidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimLocalidade')),
                ('cd_mes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimMes')),
                ('cd_plano', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.DimPlano')),
            ],
        ),
    ]
