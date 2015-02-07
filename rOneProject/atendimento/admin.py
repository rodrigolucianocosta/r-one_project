#coding:utf-8
from django.contrib import admin
from models import Atendimento,AtendimentoFamiliar,Pessoa,Medico,Paciente,Cid
# Register your models here.

class AtendimentoAdmin(admin.ModelAdmin):
	list_display = ['TipoAtendimento','DataAtendimento','Paciente','SalaAtendimento']
	save_as=True

class AtendimentoFamiliarAdmin(admin.ModelAdmin):
	list_display = ['TipoAtendimento']
	save_as=True

class MedicoAdmin(admin.ModelAdmin):
	list_display = ['NomePessoa','Crm','Especialidade']
	save_as=True

	list_filter = ['Crm']
	save_as = True	

class PacienteAdmin(admin.ModelAdmin):
	list_display = ['NomePessoa','CartaoSus']
	save_as = True		

class CidAdmin(admin.ModelAdmin):
	list_display =	['ciddescricao','CodigoPrincipal','SubCodigo']
	save_as = True 	

#deve sempre ser colocado como tupla(em pares)
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Cid,CidAdmin)
admin.site.register(Atendimento,AtendimentoAdmin)
admin.site.register(AtendimentoFamiliar,AtendimentoFamiliarAdmin)
