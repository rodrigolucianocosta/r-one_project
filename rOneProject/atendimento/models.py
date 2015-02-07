#coding:utf-8
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from localflavor.br.br_states import STATE_CHOICES
# Create your models here.

TIPO_ATENDIMENTO = [
      
      ('A','RETORNO'),
      ('B','CONSULTA'),
      ('C','AGENDAMENTO')

]

SEXO_OPCOES = [
        ('M','Masculino'),
        ('F','Feminino')
        ]


class Pessoa(models.Model):
	NomePessoa = models.CharField('Nome',max_length=100, null=True)
	Cpf = models.CharField('Cpf',max_length=11,null=True)
	Rg = models.CharField('Rg',max_length=20,null=True, )
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	Etinia = models.CharField('Etinia',max_length=10,null=True)
	NascimentoData = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=8,null=True)
	Celular = models.CharField(max_length=9,unique=True,null=True)
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
	Especialidade = models.CharField('Especialidade',max_length=20,null=True)
	
	class Meta:
		verbose_name = "Medico"
		verbose_name_plural = "Medico"


	def  __unicode__(self):
		#super(Pessoa, self).__init__(*args, **kwargs)
		return self.Crm
		
class Paciente(Pessoa):
	
	CartaoSus = models.CharField('Cartao Sus',max_length=20,null=True)
	class Meta:
		verbose_name = "Paciente"
		verbose_name_plural = "Paciente"
	def __unicode__(self):
		#super(Pessoa, self).__init__(*args, **kwargs)
		return self.CartaoSus

	
class Cid(models.Model):
	CodigoPrincipal = models.CharField('Codigo do Cid',max_length=5,null=True)
	SubCodigo = models.CharField('SubCodigo do Cid',max_length=2,null=True,blank=True)
	ciddescricao = models.CharField('descriacao do cid',max_length=100, null=True)

	def __unicode__(self):
		return self.ciddescricao
#----------------------------------------------------------------------------------------------

class Atendimento (models.Model):
	Paciente = models.ForeignKey('Paciente',verbose_name="Paciente",null=False)
	Medico = models.ForeignKey('Medico',verbose_name="Medico",null=False)
	SalaAtendimento = models.IntegerField('Sala de Atendimento',max_length=2,null=True)
	TipoAtendimento = models.CharField('Tipo de Atendimento',max_length=1,choices=TIPO_ATENDIMENTO,null=True)
	DataAtendimento = models.DateTimeField('Data de Atendimento',null=True)
	ResponsavelMarcacao = models.CharField('Responsavel pela Marcacao',max_length=100,null=True)
	class Meta:
		verbose_name = "Atendimento"
		verbose_name_plural = "Atendimento"
	
	def __unicode__(self):
		return self.TipoAtendimento


class AtendimentoFamiliar(models.Model):
	Paciente = models.ForeignKey('Paciente',verbose_name='Paciente',null=False)
	TipoAtendimento = models.CharField('Tipo de atendimento',max_length=1,choices=TIPO_ATENDIMENTO,null=True)
	SalaAtendimento = models.CharField('Sala de Atendimento',max_length=2,null=False)
	DataAtendimento = models.DateTimeField('Data de Atendimento',null=True)
	ResponsavelMarcacao = models.CharField('Responsavel pela Marcacao',max_length=20,null=True)

	
	
	class Meta:
		verbose_name = "Atendimento Familiar"
		verbose_name_plural = "Atendimento Familiar"
	

	def __unicode__(self):
		return "%s - %s" % (self.AtendimentoFamiliar.TipoAtendimento,self.AtendimentoFamiliar.InicioInscricao)

