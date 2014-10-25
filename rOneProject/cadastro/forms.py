#coding:utf-8
from django import forms
from localflavor.br.forms import BRCPFField

class PessoaForm(forms.ModelForm):

	CPF = BRCPFField()

		exclude = ['URL']