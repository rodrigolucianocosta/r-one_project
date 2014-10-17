#coding:utf-8
from django.contrib import admin
from models import Pessoa
from models import PessoaForm

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    
    form PessoaForm

	list_display = ['Nome']
	list_filter = ['Sexo']
	search_fields = ['Nome','Cpf']
	save_as = True 

class EnderecoAdmin(admin.ModelAdmin):
	list_display = ['Rua']
	save_as = True



#deve sempre ser colocado como tupla(em pares)
admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Endereco,EnderecoAdmin)
