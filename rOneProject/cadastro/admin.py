#coding:utf-8
from django.contrib import admin
from models import Pessoa
from forms import PessoaForm

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    
       form = PessoaForm

       list_display = ['NomePessoa','Cpf']
       list_filter = ['Sexo']
       search_fields = ['NomePessoa','Cpf']


	#save_as = True 



#deve sempre ser colocado como tupla(em pares)
admin.site.register(Pessoa,PessoaAdmin)

