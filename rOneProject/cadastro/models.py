#coding:utf-8
from django.db import models
#from django.core.validators import MinValueValidator,MaxvalueValidator
# Create your models here.

TIPO_CADASTRO = [
      
      ('A', 'CADASTRO PESSOAL'),
      ('B', 'CADASTRO CONSULTA'),
      ('C', 'ATENDIMENTO FAMILIAR')


]

class Cadastros(models.Model):
	NomeCadastro = models.CharField('Nome do Cadastro',max_length=100, null=True)
	DataMatricula = models.DateField('Data de Cadastro',null=True)

class Meta:
	verbose_name = "Macro Cadastro"
	verbose_name_plural = "Macro Cadastros"

def __unicode__(self):
	return self.NomeCadastro

class SubCadastro(models.Model):
	Cadastro =  models.ForeignKey(Cadastros, verbose_name = "Cadastro",null=False)
	NomeSubCadastro = models.CharField('Nome NomeSubCadastro',max_length=100,null=False)
	TipoSubCadastro = models.CharField('Tipo SubEvento',max_length=1)
	#Responsavel = models.ForeignKey()

	class Meta:
		verbose_name = "SubCadastro"
		verbose_name_plural = "SubCadastros"

	def __unicode__(self):
		return self.NomeSubCadastro

