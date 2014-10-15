# _*_ coding utf-8 _*_
from django.contrib import admin
from models import Cadastros
from models import SubCadastro

# Register your models here.

class CadastrosAdmin(admin.ModelAdmin):
	list_display = ['NomeCadastro']
	#list_filter = ['nome_do_aluno']
	#search_fields = ['']
	save_as = True 
	
class SubCadastroAdmin(admin.ModelAdmin):
	list_display = ['NomeSubCadastro']
	#list_filter = ['nome_do_aluno']
	#search_fields = ['']
	save_as = True 


#deve sempre ser colocado como tupla(em pares)
admin.site.register(Cadastros,CadastrosAdmin)
admin.site.register(SubCadastro,SubCadastroAdmin)