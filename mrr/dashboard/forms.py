from django import forms


class PeriodoForm(forms.Form):
    dt_inicio = forms.DateField(label="Início")
    dt_fim = forms.DateField(label="Fim")