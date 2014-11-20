#coding:utf-8
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from cadastro.models import Paciente

# Create your models here.

TIPO_ATENDIMENTO = [
      
      ('A','RETORNO'),
      ('B','CONSULTA'),
      ('C', 'AGENDAMENTO')

]


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
	AtendimentoF = models.ForeignKey(Atendimento,verbose_name="Atendimento Familiar",null=False)
	AtendimentoFamiliar = models.CharField('Atendimento Familiar',max_length=100,null=True)
	TipoAtendimento = models.CharField('Tipo SubEvento',max_length=1,choices=TIPO_ATENDIMENTO,null=True)
	#Responsavel = models.ForeignKey(Pessoa,verbose_name="Responsavel SubEvento",null=True)
	DataSubEvento = models.DateField('Data SubEvento',null=True)
	DuracaoSubEvento = models.IntegerField('Duracao SubEvento',null=True, help_text="Informar duração em minutos")
	LocalSubEvento = models.CharField('Local Subevento',max_length=100,null=True)
	NumParticipantesSubEvento = models.IntegerField('Numero de Participantes SubEvento',validators=[MinValueValidator(1),MaxValueValidator(1000)],null=True)
	InicioInscricao = models.DateField('Data inicio da inscriçao',null=True)
	FimInscricao = models.DateField('Data Fim da inscricao',null=True)
	
	class Meta:
		verbose_name = "Atendimento Familiar"
		verbose_name_plural = "Atendimento Familiar"

	def __unicode__(self):
		return "%s - %s" % (self.Atendimento.SalaAtendimento,self.AtendimentoFamiliar.AtendimentoF)

