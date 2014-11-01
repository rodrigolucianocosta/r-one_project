from django.contrib import admin
from models import Atendimento
from models import AtendimentoFamiliar
# Register your models here.

class AtendimentoAdmin(admin.ModelAdmin):
	list_display = ['SalaAtendimento']
	save_as=True

class AtendimentoFamiliarAdmin(admin.ModelAdmin):
	list_display = ['AtendimentoFamiliar']
	save_as=True

admin.site.register(Atendimento,AtendimentoAdmin)
admin.site.register(AtendimentoFamiliar,AtendimentoFamiliarAdmin)
