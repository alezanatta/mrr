from django.db import models, connection

from datetime import date
from datetime import datetime

from .graficos import get_gauge
from .graficos import get_pie
from .graficos import get_bar
from .graficos import get_line

import pandas as pd
import plotly.express as px

class ControleVersao(models.Model):
    cd_versao = models.AutoField(primary_key=True, serialize=True, auto_created=True)
    dt_versao = models.DateField(default=date.today)
    fato_versao = models.IntegerField(default=1, unique=True)

class DimSegmento(models.Model):
    cd_segmento = models.AutoField(primary_key=True, serialize=True, auto_created=True)
    nm_segmento = models.CharField(max_length=75, unique=True)

class DimCliente(models.Model):
    cd_cliente = models.AutoField(primary_key=True, serialize=True, auto_created=True)
    nr_cliente = models.IntegerField()
    nm_cliente = models.CharField(max_length=100)

    class Meta:
        unique_together = ("nr_cliente", "nm_cliente")

class DimLocalidade(models.Model):
    cd_localidade = models.AutoField(primary_key=True, serialize=True, auto_created=True)
    nm_cidade = models.CharField(max_length=75)
    nm_estado = models.CharField(max_length=75)

    class Meta:
        unique_together = ("nm_cidade", "nm_estado")

class DimPlano(models.Model):
    cd_plano = models.AutoField(primary_key=True, serialize=True, auto_created=True)
    nm_plano = models.CharField(max_length=75, unique=True)

class DimDia(models.Model):
    cd_dia = models.AutoField(primary_key=True, serialize=True, auto_created=True)
    dia = models.IntegerField(unique=True)

class DimMes(models.Model):
    cd_mes = models.AutoField(primary_key=True, serialize=True, auto_created=True)
    nr_mes = models.IntegerField(unique=True)
    nm_nr_mes = models.CharField(max_length=2, blank=True, null=True)
    nm_mes = models.CharField(max_length=10, unique=True)
    sg_mes = models.CharField(max_length=3, unique=True)

class DimAno(models.Model):
    cd_ano = models.AutoField(primary_key=True, serialize=True, auto_created=True)
    ano = models.IntegerField(unique=True)

class FatoMrr(models.Model):
    cd_fato_mrr = models.AutoField(primary_key=True, serialize=True, auto_created=True)
    cd_cliente = models.ForeignKey(DimCliente, on_delete=models.PROTECT)
    cd_localidade = models.ForeignKey(DimLocalidade, on_delete=models.PROTECT)
    cd_plano = models.ForeignKey(DimPlano, on_delete=models.PROTECT)
    cd_dia = models.ForeignKey(DimDia, on_delete=models.PROTECT)
    cd_mes = models.ForeignKey(DimMes, on_delete=models.PROTECT)
    cd_ano = models.ForeignKey(DimAno, on_delete=models.PROTECT)
    periodicidade = models.IntegerField(default=1)
    vl_mrr = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    vl_cancelamento = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    vl_expansao = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    sn_novo = models.BooleanField(default=False)
    sn_cancelado = models.BooleanField(default=False)
    sn_renascido = models.BooleanField(default=False)

    @staticmethod
    def mrr(dt_inicio, dt_fim=str(date.today())):

        mes_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").month
        mes_fim = datetime.strptime(dt_fim, "%Y-%m-%d").month
        ano_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").year 
        ano_fim = datetime.strptime(dt_fim, "%Y-%m-%d").year

        query = f"""SELECT sum(vl_mrr) as total FROM dashboard_fatomrr a
        INNER JOIN dashboard_dimmes b ON a.cd_mes_id = b.cd_mes
        INNER JOIN dashboard_dimano c ON a.cd_ano_id = c.cd_ano
        AND b.nr_mes >= {mes_inicio}
        AND b.nr_mes <= {mes_fim}
        AND c.ano >= {ano_inicio}
        AND c.ano <= {ano_fim}
        AND sn_cancelado = {False}
        """
        df = pd.read_sql(query, connection)
        get_gauge(df.iloc[0]["total"], "Receita Mensal","mrr")

    @staticmethod
    def new_mrr(dt_inicio, dt_fim=str(date.today())):

        mes_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").month
        mes_fim = datetime.strptime(dt_fim, "%Y-%m-%d").month
        ano_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").year 
        ano_fim = datetime.strptime(dt_fim, "%Y-%m-%d").year

        query = f"""SELECT sum(vl_mrr) as total FROM dashboard_fatomrr a
        INNER JOIN dashboard_dimmes b ON a.cd_mes_id = b.cd_mes
        INNER JOIN dashboard_dimano c ON a.cd_ano_id = c.cd_ano
        AND b.nr_mes >= {mes_inicio}
        AND b.nr_mes <= {mes_fim}
        AND c.ano >= {ano_inicio}
        AND c.ano <= {ano_fim}
        AND sn_cancelado = {False}
        AND sn_novo = {True}
        """
        df = pd.read_sql(query, connection)
        get_gauge(df.iloc[0]["total"], "Nova Receita","new_mrr")

    @staticmethod
    def expansion_mrr(dt_inicio, dt_fim=str(date.today())):
        mes_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").month
        mes_fim = datetime.strptime(dt_fim, "%Y-%m-%d").month
        ano_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").year 
        ano_fim = datetime.strptime(dt_fim, "%Y-%m-%d").year

        query = f"""SELECT sum(vl_expansao) as total FROM dashboard_fatomrr a
        INNER JOIN dashboard_dimmes b ON a.cd_mes_id = b.cd_mes
        INNER JOIN dashboard_dimano c ON a.cd_ano_id = c.cd_ano
        AND b.nr_mes >= {mes_inicio}
        AND b.nr_mes <= {mes_fim}
        AND c.ano >= {ano_inicio}
        AND c.ano <= {ano_fim}
        AND sn_cancelado = {False}
        AND vl_expansao >= 0
        """
        df = pd.read_sql(query, connection)
        get_gauge(df.iloc[0]["total"], "Receita em expansão","expansion_mrr")
    
    @staticmethod
    def contraction_mrr(dt_inicio, dt_fim=str(date.today())):
        mes_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").month
        mes_fim = datetime.strptime(dt_fim, "%Y-%m-%d").month
        ano_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").year 
        ano_fim = datetime.strptime(dt_fim, "%Y-%m-%d").year

        query = f"""SELECT sum(vl_expansao) as total FROM dashboard_fatomrr a
        INNER JOIN dashboard_dimmes b ON a.cd_mes_id = b.cd_mes
        INNER JOIN dashboard_dimano c ON a.cd_ano_id = c.cd_ano
        AND b.nr_mes >= {mes_inicio}
        AND b.nr_mes <= {mes_fim}
        AND c.ano >= {ano_inicio}
        AND c.ano <= {ano_fim}
        AND sn_cancelado = {False}
        AND vl_expansao <= 0
        """
        df = pd.read_sql(query, connection)
        get_gauge(df.iloc[0]["total"], "Receita em contração","contraction_mrr")
    
    @staticmethod
    def canceled_mrr(dt_inicio, dt_fim=str(date.today())):
        
        mes_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").month
        mes_fim = datetime.strptime(dt_fim, "%Y-%m-%d").month
        ano_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").year 
        ano_fim = datetime.strptime(dt_fim, "%Y-%m-%d").year

        query = f"""SELECT sum(vl_mrr) as total FROM dashboard_fatomrr a
        INNER JOIN dashboard_dimmes b ON a.cd_mes_id = b.cd_mes
        INNER JOIN dashboard_dimano c ON a.cd_ano_id = c.cd_ano
        AND b.nr_mes >= {mes_inicio}
        AND b.nr_mes <= {mes_fim}
        AND c.ano >= {ano_inicio}
        AND c.ano <= {ano_fim}
        AND sn_cancelado = {True}
        """
        df = pd.read_sql(query, connection)
        get_gauge(df.iloc[0]["total"], "Receita cancelada","canceled_mrr")


    @staticmethod
    def ressurected_mrr(dt_inicio, dt_fim=str(date.today())):
        
        mes_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").month
        mes_fim = datetime.strptime(dt_fim, "%Y-%m-%d").month
        ano_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").year 
        ano_fim = datetime.strptime(dt_fim, "%Y-%m-%d").year

        query = f"""SELECT sum(vl_mrr) as total FROM dashboard_fatomrr a
        INNER JOIN dashboard_dimmes b ON a.cd_mes_id = b.cd_mes
        INNER JOIN dashboard_dimano c ON a.cd_ano_id = c.cd_ano
        AND b.nr_mes >= {mes_inicio}
        AND b.nr_mes <= {mes_fim}
        AND c.ano >= {ano_inicio}
        AND c.ano <= {ano_fim}
        AND sn_renascido = {True}
        """
        df = pd.read_sql(query, connection)
        get_gauge(df.iloc[0]["total"], "Receita de retorno","ressurected_mrr")


    @staticmethod
    def tendencia_mrr(dt_inicio, dt_fim=str(date.today())):
        mes_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").month
        ano_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").year 

        query = f"""SELECT sum(vl_mrr) as total, TO_DATE(CONCAT(b.nm_nr_mes, c.ano), 'MMYYYY') as periodo FROM dashboard_fatomrr a
        INNER JOIN dashboard_dimmes b ON a.cd_mes_id = b.cd_mes
        INNER JOIN dashboard_dimano c ON a.cd_ano_id = c.cd_ano
        AND b.nr_mes >= {mes_inicio}
        AND c.ano >= {ano_inicio}
        AND sn_cancelado = {False}
        GROUP BY periodo
        ORDER BY periodo
        """
        df = pd.read_sql(query, connection)
        df["periodo"] = pd.to_datetime(df["periodo"])
        
        get_line(df, "periodo", "total", "tendencia_mrr", "Variação de Receita por Período")
        #get_gauge(df["total"].iloc[0], "Receita cancelada","canceled_mrr")
    
    @staticmethod
    def localidade_valor(dt_inicio, dt_fim=str(date.today())):

        mes_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").month
        mes_fim = datetime.strptime(dt_fim, "%Y-%m-%d").month
        ano_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").year 
        ano_fim = datetime.strptime(dt_fim, "%Y-%m-%d").year

        query = f""" SELECT sum(a.vl_mrr) as Receita, b.nm_estado as Estado
        FROM dashboard_fatomrr a
        INNER JOIN dashboard_dimlocalidade b ON a.cd_localidade_id = b.cd_localidade
        INNER JOIN dashboard_dimmes d ON a.cd_mes_id = d.cd_mes
        INNER JOIN dashboard_dimano c ON a.cd_ano_id = c.cd_ano
        AND d.nr_mes >= {mes_inicio}
        AND d.nr_mes <= {mes_fim}
        AND c.ano >= {ano_inicio}
        AND c.ano <= {ano_fim}
        GROUP BY b.nm_estado
        ORDER BY Receita DESC
        LIMIT 10
        """
        df = pd.read_sql(query, connection)
        get_bar(df, "estado", "receita", "receita_localidade", "Top 10 Receita por Estado", "Bluyl")

    @staticmethod
    def localidade_cliente(dt_inicio, dt_fim=str(date.today())):
        
        mes_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").month
        mes_fim = datetime.strptime(dt_fim, "%Y-%m-%d").month
        ano_inicio = datetime.strptime(dt_inicio, "%Y-%m-%d").year 
        ano_fim = datetime.strptime(dt_fim, "%Y-%m-%d").year

        query = f""" SELECT count(DISTINCT a.cd_cliente_id) as Clientes, b.nm_estado as Estado
        FROM dashboard_fatomrr a
        INNER JOIN dashboard_dimlocalidade b ON a.cd_localidade_id = b.cd_localidade
        INNER JOIN dashboard_dimmes d ON a.cd_mes_id = d.cd_mes
        INNER JOIN dashboard_dimano c ON a.cd_ano_id = c.cd_ano
        AND d.nr_mes >= {mes_inicio}
        AND d.nr_mes <= {mes_fim}
        AND c.ano >= {ano_inicio}
        AND c.ano <= {ano_fim}
        GROUP BY b.nm_estado
        ORDER BY Clientes DESC
        LIMIT 10
        """

        df = pd.read_sql(query, connection)
        #get_pie(df, "cliente", "estado", "cli_localidade", "Clientes por localidade")
        get_bar(df, "estado", "clientes", "cli_localidade", "Top 10 Total de Cliente por Estados")

    @staticmethod
    def get_dashboard(dt_inicio, dt_fim=str(date.today())):
        FatoMrr.mrr(dt_inicio, dt_fim)
        FatoMrr.new_mrr(dt_inicio, dt_fim)
        FatoMrr.expansion_mrr(dt_inicio, dt_fim)
        FatoMrr.contraction_mrr(dt_inicio, dt_fim)
        FatoMrr.canceled_mrr(dt_inicio, dt_fim)
        FatoMrr.ressurected_mrr(dt_inicio, dt_fim)
        FatoMrr.tendencia_mrr(dt_inicio, dt_fim)
        FatoMrr.localidade_cliente(dt_inicio, dt_fim)
        FatoMrr.localidade_valor(dt_inicio, dt_fim)


class FatoSegmento(models.Model):
    cd_fato_segmento = models.IntegerField(primary_key=True, serialize=True, auto_created=True)
    cd_segmento = models.ForeignKey(DimSegmento, on_delete=models.PROTECT)
    cd_localidade = models.ForeignKey(DimLocalidade, on_delete=models.PROTECT)
    cd_plano = models.ForeignKey(DimPlano, on_delete=models.PROTECT)
    cd_mes = models.ForeignKey(DimMes, on_delete=models.PROTECT)
    cd_ano = models.ForeignKey(DimAno, on_delete=models.PROTECT)
    vl_mrr = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    vl_cancelamento = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)

    @staticmethod
    def segmento_cancelamento(dt_inicio, dt_fim=date.today()):
        pass

    @staticmethod
    def segmento_localidade(dt_inicio, dt_fim=date.today()):
        pass

    @staticmethod
    def segmento_mrr(dt_inicio, dt_fim=date.today()):
        pass
