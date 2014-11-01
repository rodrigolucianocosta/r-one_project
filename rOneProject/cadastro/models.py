#coding:utf-8
from django.db import models
from localflavor.br.br_states import STATE_CHOICES
# Create your models here.


SEXO_OPCOES = [
        ('M','Masculino'),
        ('F','Feminino')

        ]

class TipoUsuario(models.Model):
	tipo =models.CharField('Tipo de Usuario',max_length=50,null=True)

	def __unicode__(self):
		return self.tipo        


class Pessoa(models.Model):
	NomePessoa = models.CharField('Nome',max_length=100, null=True)
	Cpf = models.CharField('Cpf',max_length=11,null=True)
	Rg = models.CharField('Rg',max_length=20,null=True, )
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	Etinia = models.CharField('Etinia',max_length=10,null=True)
	NascimentoData = models.DateField('Data de Nascimento',null=True)
	Telefone = models.IntegerField('Telefone',max_length=10,null=True)
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

class Medico(Pessoa):
	Crm = models.CharField('Crm',max_length=10, null=True)
	#Especialidade = models.CharField('Especialidade',max_length=20,nul=True)
	def  __unicode__(self):
		super(NomePessoa, self).__init__(*args, **kwargs)
		return self.Especialidade
		
class Paciente(Pessoa):
	#cidAdesao = models.ForeignKey(cidAdesao,verbose_name="numero do cid",null=True)
	#TipoUsuario = models.ForeignKey(TipoUsuario,verbose_name="Tipo de Usuario",null=True)
	CartaoSus = models.CharField('Cartao Sus',max_length=20,null=True)
	'''problemas com unicode'''
	def __unicode__(self):
    		#super(CharField, self).__init__(*args, **kwargs)   
		return self.CartaoSus

class Cid(models.Model):
	CodigoPrincipal = models.CharField('Codigo do Cid',max_length=10,null=True)
	SubCodigo = models.CharField('SubCodigo do Cid',max_length=2,null=True)
	ciddescricao = models.CharField('descriacao do cid',max_length=100, null=True)

	def __unicode__(self):
		super(CodigoPrincipal, self).__init__(*args, **kwargs)
		return self.Cid
