#coding:utf-8
from django.db import models
from localflavor.br.br_states import STATE_CHOICES
# Create your models here.


SEXO_OPCOES = [
        ('M','Masculino'),
        ('F','Feminino')

        ]


class Pessoa(models.Model):
<<<<<<< HEAD
	
	cid = models.IntegerField('Cid',null=True)
=======
	#cid = models.IntegerField('Cid',null=True)
>>>>>>> 538bcf32440d57b1f3af72717cfb30f7533d5a4d
	NomePessoa = models.CharField('Nome',max_length=100, null=True)
	Cpf = models.CharField('Cpf',max_length=11,null=True)
	Rg = models.CharField('Rg',max_length=20,null=True, )
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.IntegerField('Telefone',max_length=15,null=True)
	Celular = models.IntegerField(max_length=10,unique=True,null=True)
	NomeMae = models.CharField('Nome da Mae',max_length=50,null=True)
	NomePai = models.CharField('Nome do Pai',max_length=50,null=True)
	Rua = models.CharField('Nome da Rua',max_length=100,null=True)
	numero = models.IntegerField('numero',max_length=5,null=True)
	complemento = models.CharField('complemento',max_length=10,null=True)
	bairro = models.CharField('Bairro',max_length=100,null=True)
	cidade = models.CharField('Cidade',max_length=100,null=True)
	uf = models.CharField('UF',max_length=2,choices=STATE_CHOICES,null=True)
	


	def __unicode__(self):
		return self.NomePessoa
'''
class Medico(Pessoa):
	Crm = models.CharField('CRM',max_length=)

class Atendimento(models.Model):
	Paciente = models.OneToOneField(Pessoa)
	DataConsulta = models.DateField('data da consulta',null=True)
	#NomeMedico = 

	#def __unicode__(self):
	#	return self.DataConsulta
'''
