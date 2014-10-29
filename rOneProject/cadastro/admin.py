#coding:utf-8
from forms import PessoaForm
from django.contrib import admin
from models import Pessoa,TipoUsuario,Atendimento,Medico,Paciente,cidAdesao,AtendimentoFamiliar
from forms import PessoaForm
# Register your models here.

'''	class PessoaAdmin(admin.ModelAdmin):
		form = PessoaForm
    

    list_display = ['NomePessoa','Celular','NomeMae']
    list_filter = ['NomeMae']
    search_fields = ['NomePessoa','Cpf']
    save_as = True
'''

class AtendimentoAdmin(admin.ModelAdmin):
	list_display = ['DataConsulta']
	save_as = True

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

class AtendimentoFamiliarAdmin(admin.ModelAdmin):
	list_display =	['PlanoIntervencao']
	save_as = True	


#deve sempre ser colocado como tupla(em pares)
#admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Atendimento,AtendimentoAdmin)
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(TipoUsuario,TipoUsuarioAdmin)
admin.site.register(cidAdesao,CidAdesaoAdmin)
admin.site.register(AtendimentoFamiliar,AtendimentoFamiliarAdmin)