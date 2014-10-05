# _*_ coding utf-8 _*_
from django.contrib import admin
from models import ficha_de_matricula
# Register your models here.

class displayNome(admin.ModelAdmin):
	list_display = ['nome_do_aluno','dia_Atendimento','horario_atendimento']
	#list_filter = ['nome_do_aluno']
	search_fields = ['nome_do_aluno']
	save_as = True 
	date_hierarchy = 'data_matricula'


admin.site.register(ficha_de_matricula,displayNome)