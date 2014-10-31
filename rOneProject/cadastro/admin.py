#coding:utf-8
from forms import PessoaForm
from django.contrib import admin
from models import Pessoa
from models import TipoUsuario,Medico,Paciente,cidAdesao
from forms import PessoaForm
# Register your models here.


class MedicoAdmin(admin.ModelAdmin):
	form = PessoaForm

	list_filter = ['Crm']
	save_as = True	

class PacienteAdmin(admin.ModelAdmin):
	list_display = ['NomePessoa','CartaoSus']
	save_as = True		

class TipoUsuarioAdmin(admin.ModelAdmin):
	list_display = ['tipo']	
	save_as = True

class CidAdesaoAdmin(admin.ModelAdmin):
	list_display =	['cidPessoa']
	save_as = True 	

'''class AtendimentoFamiliarAdmin(admin.ModelAdmin):
	list_display =	['PlanoIntervencao']
	save_as = True	

'''
#deve sempre ser colocado como tupla(em pares)
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(TipoUsuario,TipoUsuarioAdmin)
admin.site.register(cidAdesao,CidAdesaoAdmin)
