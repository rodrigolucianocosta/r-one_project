#coding:utf-8
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from localflavor.br.br_states import STATE_CHOICES
# Create your models here.

TIPO_ATENDIMENTO = [
      
      ('A','RETORNO'),
      ('B','CONSULTA'),
      ('C', 'AGENDAMENTO')

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
	Especialidade = models.CharField('Especialidade',max_length=20,null=True)
	
	def  __unicode__(self):
		super(NomePessoa, self).__init__(*args, **kwargs)
		return self.Crm
		
class Paciente(Pessoa):
	CartaoSus = models.CharField('Cartao Sus',max_length=20,null=True)
	'''problemas com unicode'''
	def __unicode__(self):
		super(Pessoa, self).__init__(*args, **kwargs)
		return self.CartaoSus

	
class Cid(models.Model):
	CodigoPrincipal = models.CharField('Codigo do Cid',max_length=10,null=True)
	SubCodigo = models.CharField('SubCodigo do Cid',max_length=2,null=True,blank=True)
	ciddescricao = models.CharField('descriacao do cid',max_length=100, null=True)

	def __unicode__(self):
		return self.ciddescricao
#----------------------------------------------------------------------------------------------

class Atendimento (models.Model):
	SalaAtendimento = models.IntegerField('Sala de Atendimento',max_length=2,null=True)
	TipoAtendimento = models.CharField('Tipo de Atendimento',max_length=1,choices=TIPO_ATENDIMENTO,null=True)
	DataAtendimento = models.DateField('Data de Atendimento',null=True)
	ResponsavelMarcacao = models.CharField('Responsavel pela Marcacao',max_length=100,null=True)

	#InicioInscricao = models.DateField('Data inicio da inscriçao',null=True)
	#FimInscricao = models.DateField('Data Fim da inscricao',null=True)
	
	class Meta:
		verbose_name = "Atendimento"
		verbose_name_plural = "Atendimentos"
	
	def __unicode__(self):
		return self.SalaAtendimento


class AtendimentoFamiliar(models.Model):
	TipoAtendimento = models.CharField('Tipo SubEvento',max_length=1,choices=TIPO_ATENDIMENTO,null=True)
	InicioInscricao = models.DateField('Data inicio da inscriçao',null=True)
	FimInscricao = models.DateField('Data Fim da inscricao',null=True)
	'''AtendimentoF = models.ForeignKey(Atendimento,verbose_name="Atendimento Familiar",null=False)
	AtendimentoFamiliar = models.CharField('Atendimento Familiar',max_length=100,null=True)
	TipoAtendimento = models.CharField('Tipo SubEvento',max_length=1,choices=TIPO_ATENDIMENTO,null=True)
	#Responsavel = models.ForeignKey(Pessoa,verbose_name="Responsavel SubEvento",null=True)
	DataSubEvento = models.DateField('Data SubEvento',null=True)
	DuracaoSubEvento = models.IntegerField('Duracao SubEvento',null=True, help_text="Informar duração em minutos")
	LocalSubEvento = models.CharField('Local Subevento',max_length=100,null=True)
 NumParticipantesSubEvento = models.IntegerField('Numero de Participantes SubEvento',validators=[MinValueValidator(1),MaxValueValidator(1000)],null=True)
	InicioInscricao = models.DateField('Data inicio da inscriçao',null=True)
	FimInscricao = models.DateField('Data Fim da inscricao',null=True)
	'''
	class Meta:
		verbose_name = "Atendimento Familiar"
		verbose_name_plural = "Atendimento Familiar"
	

	def __unicode__(self):
		return "%s - %s" % (self.AtendimentoFamiliar.TipoAtendimento,self.AtendimentoFamiliar.InicioInscricao)

