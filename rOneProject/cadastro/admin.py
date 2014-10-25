#coding:utf-8
from django.contrib import admin
from models import Pessoa
from forms import PessoaForm
#from models import Atendimento
# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    
       

    list_display = ['NomePessoa','Cpf']
    list_filter = ['NomePessoa']
    search_fields = ['NomePessoa','Cpf']
    save_as = True

'''class AtendimentoAdmin(admin.ModelAdmin):
	list_display = ['DataConsulta']
	save_as = True
'''

#deve sempre ser colocado como tupla(em pares)
admin.site.register(Pessoa,PessoaAdmin)
#admin.site.register(Atendimento,AtendimentoAdmin)

